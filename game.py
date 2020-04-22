import pygame


class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.isJump = False
        self.jumpInterval = -8

    def moveLeft(self):
        self.x -= self.vel

    def moveRight(self):
        self.x += self.vel

    def jump(self):
        self.isJump = True

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, value):
        self.x = value

    def setY(self, value):
        self.y = value

    def getVel(self):
        return self.vel

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getIsJump(self):
        return self.isJump

    def getJumpInterval(self):
        return self.jumpInterval

    def setIsJump(self, value):
        self.isJump = value

    def setJumpInterval(self, value):
        self.jumpInterval = value


pygame.init()
win_sizex = 1000
win_sizey = 500

win = pygame.display.set_mode((win_sizex, win_sizey))
pygame.display.set_caption("Test")

player = player(win_sizex / 2, win_sizey - 30, 30, 30)

run = True
while run:
    pygame.time.delay(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        if player.getX() >= player.getVel():
            player.moveLeft()
    if keys[pygame.K_RIGHT]:
        if player.getX() <= win_sizex - player.getWidth() - player.getVel():
            player.moveRight()
    if keys[pygame.K_SPACE]:
        if player.getIsJump() == False:
            player.jump()

    if player.getIsJump() == True:
        y = player.getY()
        jumpInterval = player.getJumpInterval()
        neg = -1
        if jumpInterval <= 8:
            if jumpInterval > 0:
                neg = 1
            y = y + (jumpInterval) ** 2 * neg
            player.setY(y)
            jumpInterval += 1
            player.setJumpInterval(jumpInterval)
        else:
            player.setIsJump(False)
            player.setJumpInterval(-8)

    win.fill((0))
    pygame.draw.rect(
        win,
        (0, 255, 0),
        (player.getX(), player.getY(), player.getWidth(), player.getHeight()),
    )
    pygame.display.update()

pygame.quit()
