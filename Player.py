from pygame import image
from Bullet import Bullet
from pygame import mixer
from State import State
class Player(State):
    def __init__(self,screen, uri):
        screen_H, screen_V = screen.get_size()
        super().__init__(screen, screen_H // 2, screen_V - 100)
        self.shipImg = image.load(uri)
        self.xChange = 5
        self.bulletSound = mixer.Sound("./resource/laser.wav")

    def show(self):
        self.screen.blit(self.shipImg, (self.X, self.Y))

    def move(self):
        if self.direction != 0:
            self.X += self.direction * self.xChange
        if self.X < 0:
            self.X = 0
        if self.X > self.screen_H-64:
            self.X = self.screen_H-64

    def fire(self):
        bullet = Bullet(self.screen, './resource/bullet.png', self.X + 20, self.Y)
        self.bulletSound.play()
        return bullet

