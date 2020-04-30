import pygame


class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velX = 0 
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
            self.x + 35, self.y + 10, 30, 45 
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
    
    def setVelX(self, value):
        self.velX = value
    
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

    def setFaceLeft(self):
        self.faceLeft = True 
        self.faceRight = False

    def getFaceRight(self):
        return self.faceRight

    def setFaceRight(self):
        self.faceRight = True 
        self.faceLeft = False

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

    def setIsIdle(self):
        self.isIdle = True 
        self.isRunning = False

    def getIsRunning(self):
        return self.isRunning

    def setIsRunning(self):
        self.isRunning = True 
        self.isIdle = False

    def updateRect(self):
        self.rect.x = self.x + 35
        self.rect.y = self.y + 10

    def getRect(self):
        return self.rect
