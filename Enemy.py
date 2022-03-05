from pygame import image
from Enemy_Bullet import Enemy_Bullet
from State import State
class Enemy(State):

    def __init__(self, screen, uri, x, y):
        super().__init__(screen, x, y)
        #self.enemyImg = image.load(uri)
        self.enemyImg1 = image.load('resource/enemy1_a.png')
        self.enemyImg2 = image.load('resource/enemy1_b.png')
        self.enemyImg = self.enemyImg1
        self.xChange = 3


    def show(self):
        self.screen.blit(self.enemyImg, (self.X, self.Y))

    def move(self):
        self.X += self.direction * self.xChange
        if self.X < 16 or self.X > self.screen_H-65:
            self.direction *= -1
            self.Y += 70
            self.X += self.direction * self.xChange
        if self.Y > self.screen_V - 120:
            self.state = "game over"

    def animate(self):
        if self.enemyImg == self.enemyImg1:
            self.enemyImg = self.enemyImg2
        else:
            self.enemyImg = self.enemyImg1

    def fire(self):
        bullet = Enemy_Bullet(self.screen, './resource/bullet2.png', self.X + 15, self.Y)
        return bullet



