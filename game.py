import pygame


class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10

    def moveLeft(self):
        self.x -= self.vel

    def moveRight(self):
        self.x += self.vel

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getVel(self):
        return self.vel

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height


pygame.init()
win_sizex = 1000
win_sizey = 500

win = pygame.display.set_mode((win_sizex, win_sizey))
pygame.display.set_caption("Test")

player = player(win_sizex / 2, win_sizey - 30, 30, 30)

run = True
while run:
    pygame.time.delay(20)
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

    win.fill((0))
    pygame.draw.rect(
        win,
        (0, 255, 0),
        (player.getX(), player.getY(), player.getWidth(), player.getHeight()),
    )
    pygame.display.update()

pygame.quit()
