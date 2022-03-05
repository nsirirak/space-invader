from pygame import image
from State import State

class Enemy_Bullet(State):
    def __init__(self, screen, uri, x, y):
        super().__init__(screen, x, y)
        self.bulletImg = image.load(uri)
        self.state = "fire"
        self.yChange = 6

    def show(self):
        self.screen.blit(self.bulletImg, (self.X, self.Y))

    def move(self):
        self.Y += self.yChange
        if self.Y > self.screen_V-50:
            self.state = "die"
