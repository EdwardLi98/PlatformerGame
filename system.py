import pygame
import os
from player import Player

game_map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

class System(object):
    def __init__(self, win_x, win_y, bg_x, bg_y):
        self.win_x = win_x
        self.win_y = win_y
        self.bg_x = bg_x
        self.bg_y = bg_y
        self.bg = False
        self.display = False
        self.run = False
        self.idle = False
        self.player = False
        self.scroll = [0, 0]
        self.tile_rect = []

    def initialiseGame(self):
        pygame.init()

        display = pygame.display.set_mode((self.win_x, self.win_y))
        self.display = display
        pygame.display.set_caption("Test")

        surface = pygame.Surface(display.get_size())
        surface = surface.convert()
        surface.fill((250, 250, 250))

        clock = pygame.time.Clock()
        bg = pygame.image.load("mountains.png").convert()
        self.bg = bg

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

        player = Player(self.win_x // 2 - 50, self.win_y - 250, 100, 55)
        self.player = player

    def drawGameStatus(self):

        bg = self.bg
        player = self.player
        bg_x = self.bg_x
        bg_y = self.bg_y
        display = self.display
        run = self.run
        idle = self.idle

        # rel_bg_x = bg_x % bg.get_rect().width
        # display.blit(bg, (rel_bg_x - bg.get_rect().width, bg_y))
        # if rel_bg_x < bg.get_rect().width:
        # display.blit(bg, (rel_bg_x, bg_y))
        # self.scroll is the amount the player has moved (left is negative, right is positive)
        self.scroll[0] += int(
            (player.getX() - self.scroll[0] - self.win_x // 2 + player.getWidth() // 2)
            / 30
        )
        self.scroll[1] += int(
            (
                player.getY()
                - self.scroll[1]
                - self.win_y
                + 200
                + player.getHeight() // 2
            )
            / 30
        )

        display.fill((0, 0, 0))
        display.blit(bg, (-self.scroll[0], -self.scroll[1]))


        #Code to draw hitbox around player (not true hit box)
        hitbox = player.getRect()
        shifted_hitbox = pygame.Rect(hitbox.x - self.scroll[0], hitbox.y - self.scroll[1], hitbox.width, hitbox.height) 
        pygame.draw.rect(self.display, (0, 255, 0), shifted_hitbox, 1)

        #tile_rect is a list of all tile rects/ Renders all tiles onto display
        tile_rect = []
        a = 0
        for layer in game_map:
            b = 0
            for tile in layer:
                rect = pygame.Rect(b*32 - self.scroll[0], a*32 - self.scroll[1], 32, 32)
                if tile != 0:
                    tile_rect.append(pygame.Rect(b*32, a*32, 32, 32))
                if tile == 1:
                    pygame.draw.rect(self.display, (255, 255, 255), rect)
                b += 1
            a += 1
        self.tile_rect = tile_rect

        #Increasing value of delay slows down player animation
        delay = 5
        if player.getIsRunning():
            if player.getWalkCount() + 1 >= delay*10:
                player.setWalkCount(0)

            if player.getFaceRight():
                display.blit(
                    run[player.getWalkCount() // delay],
                    (player.getX() - self.scroll[0], player.getY() - self.scroll[1]),
                )
                player.setIdleCount(0)
            elif player.getFaceLeft():
                display.blit(
                    pygame.transform.flip(run[player.getWalkCount() // delay], True, False),
                    (player.getX() - self.scroll[0], player.getY() - self.scroll[1]),
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
                    (player.getX() - self.scroll[0], player.getY() - self.scroll[1]),
                )
            elif player.getFaceRight():
                display.blit(
                    idle[player.getIdleCount() // 5],
                    (player.getX() - self.scroll[0], player.getY() - self.scroll[1]),
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
            collision_direction = self.detectPlayerCollision('left')
        elif self.player.getVelX() > 0:
            collision_direction = self.detectPlayerCollision('right')

        if self.player.getVelX() != 0 and collision_direction['left'] == False and collision_direction['right'] == False:
            self.player.setX(self.player.getX() + self.player.getVelX())


        #Player movement up and down
        if self.player.getVelY() < 0:
            collision_direction = self.detectPlayerCollision('up')
        elif self.player.getVelY() > 0:
            collision_direction = self.detectPlayerCollision('down') 

        if self.player.getVelY() == 0:
            self.player.setVelY(1)
        elif collision_direction['down'] == False:
            #Gravity which adds 1 to downward velocity every tick
            self.player.setVelY(self.player.getVelY() + 1)
            if collision_direction['up'] == False:
                self.player.setY(self.player.getY() + self.player.getVelY())
        else:
            self.player.setIsJump(False)


    def detectPlayerCollision(self, direction):
        collision_direction = {'up': False, 'down': False, 'left': False, 'right': False}

        rel_rect = self.player.getRect()
        #Collision check for vertical momentum
        if direction == 'down' or direction == 'up':
            rel_rect = rel_rect.move(0, self.player.getVelY())
            if direction == 'down':
                for tile in self.tile_rect:
                    if rel_rect.colliderect(tile):
                        self.player.setY(tile.top - self.player.getRect().height - 10)
                        collision_direction['down'] = True
            elif direction == 'up':
                for tile in self.tile_rect:
                    if rel_rect.colliderect(tile):
                        self.player.setY(tile.bottom - 10)
                        collision_direction['up'] = True

        #Collision check for horizontal momentum
        if direction == 'left' or direction == 'right':
            rel_rect = rel_rect.move(self.player.getVelX(), 0)
            if direction == 'left':
                for tile in self.tile_rect:
                    if rel_rect.colliderect(tile):
                        self.player.setX(tile.right - 35)
                        collision_direction['left'] = True
            elif direction == 'right':
                for tile in self.tile_rect:
                    if rel_rect.colliderect(tile):
                        self.player.setX(tile.left - self.player.getRect().width - 35)
                        collision_direction['right'] = True
            
        return collision_direction