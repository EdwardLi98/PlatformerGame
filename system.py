import pygame
import os
from player import Player


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

        player = Player(self.win_x / 2 - 100, self.win_y - 100, 30, 30)
        self.player = player

    def drawGameStatus(self):

        bg = self.bg
        player = self.player
        bg_x = self.bg_x
        bg_y = self.bg_y
        display = self.display
        run = self.run
        idle = self.idle

        rel_bg_x = bg_x % bg.get_rect().width
        display.blit(bg, (rel_bg_x - bg.get_rect().width, bg_y))
        if rel_bg_x < bg.get_rect().width:
            display.blit(bg, (rel_bg_x, bg_y))

        if player.getIsRunning():
            if player.getWalkCount() + 1 >= 30:
                player.setWalkCount(0)

            if player.getFaceRight():
                display.blit(
                    run[player.getWalkCount() // 3], (player.getX(), player.getY())
                )
                player.setIdleCount(0)
            elif player.getFaceLeft():
                display.blit(
                    pygame.transform.flip(run[player.getWalkCount() // 3], True, False),
                    (player.getX(), player.getY()),
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
                    (player.getX(), player.getY()),
                )
            elif player.getFaceRight():
                display.blit(
                    idle[player.getIdleCount() // 3], (player.getX(), player.getY())
                )

        pygame.display.update()

    def runGame(self):
        clock = pygame.time.Clock()
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            player = self.player

            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                if player.getX() >= player.getVel():
                    player.setFaceLeft(True)
                    player.setFaceRight(False)
                    player.setIsRunning(True)
                    player.setIsIdle(False)
                    player.setWalkCount(player.getWalkCount() + 1)
                    self.bg_x += 5
            elif keys[pygame.K_d]:
                if player.getX() <= self.win_x - player.getWidth() - player.getVel():
                    player.setFaceLeft(False)
                    player.setFaceRight(True)
                    player.setIsRunning(True)
                    player.setIsIdle(False)
                    player.setWalkCount(player.getWalkCount() + 1)
                    self.bg_x -= 5
            else:
                player.setIsRunning(False)
                player.setIsIdle(True)
                player.setIdleCount(player.getIdleCount() + 1)

            if keys[pygame.K_SPACE]:
                if player.getIsJump() == False:
                    player.jump()

            if player.getIsJump() == True:
                y = player.getY()
                jumpInterval = player.getJumpInterval()
                if jumpInterval <= 10:
                    y = y + (jumpInterval) * abs(jumpInterval) * 0.5
                    player.setY(y)
                    jumpInterval += 1
                    player.setJumpInterval(jumpInterval)
                else:
                    player.setIsJump(False)
                    player.setJumpInterval(-10)

            self.player = player
            self.drawGameStatus()
            clock.tick(60)

        pygame.quit()
