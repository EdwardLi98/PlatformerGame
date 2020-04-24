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
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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

        if player.getIsRunning():
            if player.getWalkCount() + 1 >= 30:
                player.setWalkCount(0)

            if player.getFaceRight():
                display.blit(
                    run[player.getWalkCount() // 3],
                    (player.getX() - self.scroll[0], player.getY() - self.scroll[1]),
                )
                player.setIdleCount(0)
            elif player.getFaceLeft():
                display.blit(
                    pygame.transform.flip(run[player.getWalkCount() // 3], True, False),
                    (player.getX() - self.scroll[0], player.getY() - self.scroll[1]),
                )
                player.setIdleCount(0)
        elif player.getIsIdle():
            if player.getIdleCount() + 1 >= 22:
                player.setIdleCount(0)
            if player.getFaceLeft():
                display.blit(
                    pygame.transform.flip(
                        idle[player.getIdleCount() // 3], True, False
                    ),
                    (player.getX() - self.scroll[0], player.getY() - self.scroll[1]),
                )
            elif player.getFaceRight():
                display.blit(
                    idle[player.getIdleCount() // 3],
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
            clock.tick(100)

        pygame.quit()

    def movement(self):

        player = self.player
        keys = pygame.key.get_pressed()
        collision_direction = self.detectPlayerCollision(player, keys)

        #Deal with keyboard presses
        if keys[pygame.K_a]:
            if player.getX() >= player.getVelX():
                player.setFaceLeft(True)
                player.setFaceRight(False)
                player.setIsRunning(True)
                player.setIsIdle(False)
                player.setWalkCount(player.getWalkCount() + 1)
                # self.bg_x += 5
                player.setX(player.getX() - player.getVelX())
        elif keys[pygame.K_d]:
            if player.getX() <= self.win_x - player.getWidth() - player.getVelX() and not collision_direction['right']:
                player.setFaceLeft(False)
                player.setFaceRight(True)
                player.setIsRunning(True)
                player.setIsIdle(False)
                player.setWalkCount(player.getWalkCount() + 1)
                # self.bg_x -= 5
                player.setX(player.getX() + player.getVelX())
        else:
            player.setIsRunning(False)
            player.setIsIdle(True)
            player.setIdleCount(player.getIdleCount() + 1)

        if keys[pygame.K_SPACE]:
            if player.getIsJump() == False:
                player.setIsJump(True)
                print("This runs")
                player.setVelY(-15)

        if player.getIsJump() == True and collision_direction['bottom']:
            player.setIsJump(False)
            #y = player.getY()
            #jumpInterval = player.getJumpInterval()
            #if jumpInterval <= 10 and not collision_direction['bottom']:
                #y = y + (jumpInterval) * abs(jumpInterval) * 0.5
                #player.setY(y)
                #jumpInterval += 1
                #player.setJumpInterval(jumpInterval)
            #else:
                #player.setIsJump(False)
                #player.setJumpInterval(-10)

        #Player gravity
        if player.getY() + player.getHeight() + player.getVelY() <= self.win_y and not collision_direction['bottom']:
            player.setY(player.getY() + player.getVelY())
        if player.getVelY() < 10:
            player.setVelY(player.getVelY() + 1)


        self.player = player

    def detectPlayerCollision(self, player, keys):
        collision_direction = {'top': False, 'bottom': False, 'left': False, 'right': False}
        player_rect = player.getRect()
        tile_rect = self.tile_rect

        #Test which side of player is colliding with tile
        for tile in tile_rect:
            if player_rect.colliderect(tile):
                #Case 1: Tile is underneath
                if tile.center
                if player_rect.bottom >= tile.top and player_rect.bottom <= tile.bottom:
                    player.setIsJump(False)
                    if not keys[pygame.K_SPACE]:
                        player.setY(tile.top - player.getHeight() + 1)
                        collision_direction['bottom'] = True
                        player.setVelY(0)
                #Case 2: Tile is to the right
                if tile.centerx > player_rect.centerx:
                    if player_rect.right >= tile.left and player_rect.right <= tile.right:
                        collision_direction['right'] = True
                        player.setX(tile.left - player.getWidth() + 1)

        return collision_direction