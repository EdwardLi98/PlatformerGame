import pygame
import os
from player import player

pygame.init()

win_sizex = 1000
win_sizey = 500
win = pygame.display.set_mode((win_sizex, win_sizey))

pygame.display.set_caption("Test")
clock = pygame.time.Clock()

bg = pygame.image.load("mountains.png").convert()
bg_x = 0
bg_y = -50
runRight = [
    pygame.image.load(os.path.join("HeroKnight\Run\HeroKnight_Run_" + str(x) + ".png"))
    for x in range(0, 10)
]

idle = [
    pygame.image.load(
        os.path.join("HeroKnight\Idle\HeroKnight_Idle_" + str(x) + ".png")
    )
    for x in range(0, 8)
]

player = player(win_sizex / 2 - 100, win_sizey - 100, 30, 30)


def drawGameStatus():
    global bg_x, bg, bg_y, player

    rel_bg_x = bg_x % bg.get_rect().width
    win.blit(bg, (rel_bg_x - bg.get_rect().width, bg_y))
    if rel_bg_x < bg.get_rect().width:
        win.blit(bg, (rel_bg_x, bg_y))

    if player.getIsRunning():
        if player.getWalkCount() + 1 >= 30:
            player.setWalkCount(0)

        if player.getFaceRight():
            win.blit(
                runRight[player.getWalkCount() // 3], (player.getX(), player.getY())
            )
            player.setIdleCount(0)
        elif player.getFaceLeft():
            win.blit(
                pygame.transform.flip(
                    runRight[player.getWalkCount() // 3], True, False
                ),
                (player.getX(), player.getY()),
            )
            player.setIdleCount(0)
    elif player.getIsIdle():
        if player.getIdleCount() + 1 >= 22:
            player.setIdleCount(0)
        if player.getFaceLeft():
            win.blit(
                pygame.transform.flip(idle[player.getIdleCount() // 3], True, False),
                (player.getX(), player.getY()),
            )
        elif player.getFaceRight():
            win.blit(idle[player.getIdleCount() // 3], (player.getX(), player.getY()))

    pygame.display.update()


# Main Loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        if player.getX() >= player.getVel():
            player.setFaceLeft(True)
            player.setFaceRight(False)
            player.setIsRunning(True)
            player.setIsIdle(False)
            player.setWalkCount(player.getWalkCount() + 1)
            bg_x += 5
    elif keys[pygame.K_d]:
        if player.getX() <= win_sizex - player.getWidth() - player.getVel():
            player.setFaceLeft(False)
            player.setFaceRight(True)
            player.setIsRunning(True)
            player.setIsIdle(False)
            player.setWalkCount(player.getWalkCount() + 1)
            bg_x -= 5
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

    # Background transition
    drawGameStatus()
    clock.tick(60)

pygame.quit()
