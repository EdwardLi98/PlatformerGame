class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.isJump = False
        self.jumpInterval = -10
        self.faceLeft = False
        self.faceRight = True
        self.walkCount = 0
        self.idleCount = 0
        self.isIdle = True
        self.isRunning = False

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
