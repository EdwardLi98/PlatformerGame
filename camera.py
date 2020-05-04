from player import Player

class Camera(object):
    def __init__(self, player, scroll_x, scroll_y, win_x, win_y):
        self.player = player
        self.scroll = [scroll_x, scroll_y]
        self.win_x = win_x
        self.win_y = win_y

    def updateCamera(self, player):
        self.scroll[0] += int(
            (player.getX() - self.scroll[0] - self.win_x // 2 + player.getWidth() // 2)
            / 20
        ) 
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