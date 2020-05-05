from player import Player
from map import Map

class Camera(object):
    def __init__(self, player, map, scroll_x, scroll_y, win_x, win_y):
        self.player = player
        self.scroll = [scroll_x, scroll_y]
        self.win_x = win_x
        self.win_y = win_y
        self.map = map

    def updateCamera(self, player):

        if player.getX() - self.win_x // 2 + player.getWidth() // 2 >= 0 and player.getX() + self.win_x // 2 + player.getWidth() // 2 <= self.map.getWidth():
            self.scroll[0] += int(
                (player.getX() - self.scroll[0] - self.win_x // 2 + player.getWidth() // 2)
                / 20
            ) 
        if player.getY() - self.win_y  + 200 + player.getHeight() // 2 >= 0 and player.getY() + self.win_y + 200 + player.getHeight() // 2 <= self.map.getHeight():
            self.scroll[1] += int(
                (
                    player.getY()
                    - self.scroll[1]
                    - self.win_y 
                    + 200
                    + player.getHeight() // 2
                )
                / 20
            )


    def applyCameraBlock(self, x, y):
        x -= self.scroll[0]
        y -= self.scroll[1]

        return (x, y) 