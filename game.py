import pygame


class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.isJump = False
        self.jumpInterval = -10

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


# def drawGameState():

pygame.init()

win_sizex = 1000
win_sizey = 500
win = pygame.display.set_mode((win_sizex, win_sizey))

pygame.display.set_caption("Test")
clock = pygame.time.Clock()

bg = pygame.image.load("mountains.png").convert()
bg_x = 0
bg_y = -50

player = player(win_sizex / 4, win_sizey - 80, 30, 30)

# Main Loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if player.getX() >= player.getVel():
            player.moveLeft()
            bg_x += 5
    if keys[pygame.K_RIGHT]:
        if player.getX() <= win_sizex - player.getWidth() - player.getVel():
            if player.getX() <= win_sizex / 2 - player.getVel():
                player.moveRight()
            bg_x -= 5
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
    rel_bg_x = bg_x % bg.get_rect().width
    win.blit(bg, (rel_bg_x - bg.get_rect().width, bg_y))
    if rel_bg_x < bg.get_rect().width:
        win.blit(bg, (rel_bg_x, bg_y))

    pygame.draw.rect(
        win,
        (102, 0, 204),
        (player.getX(), player.getY(), player.getWidth(), player.getHeight()),
    )
    pygame.display.update()
    clock.tick(60)

pygame.quit()
