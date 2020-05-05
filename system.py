import pygame
import os
from player import Player
from map import Map
from camera import Camera

class System(object):
    def __init__(self, win_x, win_y, bg_x, bg_y):
        self.win_x = win_x
        self.win_y = win_y
        self.display = False
        self.run = False
        self.idle = False
        self.player = False
        self.obstacle_rect = []
        self.interact_rect = []

    def initialiseGame(self):
        pygame.init()

        display = pygame.display.set_mode((self.win_x, self.win_y))
        self.display = display
        pygame.display.set_caption("Test")

        surface = pygame.Surface(display.get_size())
        surface = surface.convert()
        surface.fill((250, 250, 250))

        clock = pygame.time.Clock()

        # Load in all the images and sprites
        run = [
            pygame.image.load(
                os.path.join("HeroKnight\Run\HeroKnight_Run_" + str(x) + ".png")
            )
            for x in range(0, 10)
        ]

        self.run = run

        idle = [
            pygame.image.load(
                os.path.join("HeroKnight\Idle\HeroKnight_Idle_" + str(x) + ".png")
            )
            for x in range(0, 8)
        ]
        self.idle = idle

        self.map = Map(os.path.join("Maps\Map1.tmx"))
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        
        for tile_object in self.map.tmxdata.objects:
            if tile_object.name == "Player":
                self.player = Player(tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            elif tile_object.name == "Ground":
                rect = pygame.Rect(tile_object.x, tile_object.y, tile_object.width, tile_object.height)
                self.obstacle_rect.append(rect)
            elif tile_object.name == "Ladder":
                rect = pygame.Rect(tile_object.x, tile_object.y, tile_object.width, tile_object.height)
                self.interact_rect.append(rect)
                

        self.camera = Camera(self.player, self.map, 0, 0, self.win_x, self.win_y)

    def drawGameStatus(self):

        player = self.player
        display = self.display
        run = self.run
        idle = self.idle

        self.camera.updateCamera(self.player)

        display.fill((0, 0, 0))
        display.blit(self.map_img, self.camera.applyCameraBlock(0, 0))

        #Code to draw hitbox around player (not true hit box)
        #hitbox = player.getRect()
        #shifted_hitbox = pygame.Rect(self.camera.applyCameraBlock(hitbox.x, hitbox.y), (hitbox.width, hitbox.height)) 
        #pygame.draw.rect(self.display, (0, 255, 0), shifted_hitbox, 1)

        #Increasing value of delay slows down player animation
        delay = 5
        if player.getIsRunning():
            if player.getWalkCount() + 1 >= delay*10:
                player.setWalkCount(0)

            if player.getFaceRight():
                display.blit(
                    run[player.getWalkCount() // delay],
                    self.camera.applyCameraBlock(player.getX(), player.getY()),
                )
                player.setIdleCount(0)
            elif player.getFaceLeft():
                display.blit(
                    pygame.transform.flip(run[player.getWalkCount() // delay], True, False),
                    self.camera.applyCameraBlock(player.getX(), player.getY()),
                )
                player.setIdleCount(0)
        elif player.getIsIdle():
            if player.getIdleCount() + 1 >= delay*7:
                player.setIdleCount(0)
            if player.getFaceLeft():
                display.blit(
                    pygame.transform.flip(
                        idle[player.getIdleCount() // delay], True, False
                    ),
                    self.camera.applyCameraBlock(player.getX(), player.getY()),
                )
            elif player.getFaceRight():
                display.blit(
                    idle[player.getIdleCount() // 5],
                    self.camera.applyCameraBlock(player.getX(), player.getY()),
                )
        pygame.display.update()

    def runGame(self):
        player = self.player
        clock = pygame.time.Clock()
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            self.movement()
            self.drawGameStatus()
            clock.tick(60)

        pygame.quit()

    def movement(self):

        keys = pygame.key.get_pressed()

        #Deal with keyboard presses
        if keys[pygame.K_a]:
            self.player.setFaceLeft()
            self.player.setIsRunning()
            self.player.setWalkCount(self.player.getWalkCount() + 1)
            self.player.setVelX(-3)
        elif keys[pygame.K_d]:
            self.player.setFaceRight()
            self.player.setIsRunning()
            self.player.setWalkCount(self.player.getWalkCount() + 1)
            self.player.setVelX(3)
        elif keys[pygame.K_w]:
            self.player.setIsIdle()
            self.player.setIdleCount(self.player.getIdleCount() + 1)
            self.player.setVelX(0)
            if self.detectPlayerCollisionLadder():
                self.player.setVelY(-3)
        else:
            self.player.setIsIdle()
            self.player.setIdleCount(self.player.getIdleCount() + 1)
            self.player.setVelX(0)

        if keys[pygame.K_SPACE]:
            if self.player.getIsJump() == False:
                self.player.setIsJump(True)
                self.player.setVelY(-15)

        #Player movement left and right
        if self.player.getVelX() < 0:
            collision_direction = self.detectPlayerCollisionGround('left')
        elif self.player.getVelX() > 0:
            collision_direction = self.detectPlayerCollisionGround('right')

        if self.player.getVelX() != 0 and collision_direction['left'] == False and collision_direction['right'] == False:
            self.player.setX(self.player.getX() + self.player.getVelX())


        #Player movement up and down
        if self.player.getVelY() < 0:
            collision_direction = self.detectPlayerCollisionGround('up')
        elif self.player.getVelY() > 0:
            collision_direction = self.detectPlayerCollisionGround('down') 

        if self.player.getVelY() == 0:
            self.player.setVelY(1)
        elif collision_direction['down'] == False and collision_direction['up'] == False:
            self.player.setY(self.player.getY() + self.player.getVelY())
            self.player.setVelY(self.player.getVelY() + 1)
        elif collision_direction['up']:
            self.player.setVelY(1)
        else:
            self.player.setVelY(1)
            self.player.setIsJump(False)


    def detectPlayerCollisionGround(self, direction):
        collision_direction = {'up': False, 'down': False, 'left': False, 'right': False}

        rel_rect = self.player.getRect()
        #Collision check for vertical momentum
        if direction == 'down' or direction == 'up':
            rel_rect = rel_rect.move(0, self.player.getVelY())
            if direction == 'down':
                for tile in self.obstacle_rect:
                    if rel_rect.colliderect(tile):
                        self.player.setY(tile.top - self.player.getRect().height - 10)
                        collision_direction['down'] = True
            elif direction == 'up':
                for tile in self.obstacle_rect:
                    if rel_rect.colliderect(tile):
                        self.player.setY(tile.bottom - 10)
                        collision_direction['up'] = True

        #Collision check for horizontal momentum
        if direction == 'left' or direction == 'right':
            rel_rect = rel_rect.move(self.player.getVelX(), 0)
            if direction == 'left':
                for tile in self.obstacle_rect:
                    if rel_rect.colliderect(tile):
                        self.player.setX(tile.right - 35)
                        collision_direction['left'] = True
            elif direction == 'right':
                for tile in self.obstacle_rect:
                    if rel_rect.colliderect(tile):
                        self.player.setX(tile.left - self.player.getRect().width - 35)
                        collision_direction['right'] = True
            
        return collision_direction

    def detectPlayerCollisionLadder(self):

        for tile in self.interact_rect:
            if self.player.getRect().colliderect(tile):
                return True

