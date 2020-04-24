import pygame


class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velX = 2 
        self.velY = 0 
        self.isJump = False
        self.jumpInterval = -10
        self.faceLeft = False
        self.faceRight = True
        self.walkCount = 0
        self.idleCount = 0
        self.isIdle = True
        self.isRunning = False
        self.rect = pygame.Rect(
            self.x + 30, self.y + 10, self.width - 65, self.height - 10
        )

    def moveLeft(self):
        self.x -= self.vel

    def moveRight(self):
        self.x += self.vel

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, value):
        self.x = value
        self.updateRect()

    def setY(self, value):
        self.y = value
        self.updateRect()

    def getVelX(self):
        return self.velX
    
    def getVelY(self):
        return self.velY
    
    def setVelY(self, value):
        self.velY = value

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

    def getFaceLeft(self):
        return self.faceLeft

    def setFaceLeft(self, value):
        self.faceLeft = value

    def getFaceRight(self):
        return self.faceRight

    def setFaceRight(self, value):
        self.faceRight = value

    def getWalkCount(self):
        return self.walkCount

    def setWalkCount(self, value):
        self.walkCount = value

    def getIdleCount(self):
        return self.idleCount

    def setIdleCount(self, value):
        self.idleCount = value

    def getIsIdle(self):
        return self.isIdle

    def setIsIdle(self, value):
        self.isIdle = value

    def getIsRunning(self):
        return self.isRunning

    def setIsRunning(self, value):
        self.isRunning = value

    def updateRect(self):
        self.rect.x = self.x + 30
        self.rect.y = self.y + 10

    def getRect(self):
        return self.rect
