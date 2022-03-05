import math
from Player import Player
from Enemy import Enemy
from pygame import  mixer
import random

class GameControl:
    def __init__(self, screen):
        self.screen = screen
        self.screen_H, self.screen_V = screen.get_size()
        self.gameState = "run"
        # score
        self.score_value = 0
        self.bullets = []
        self.enemyBullet = []

        # create player
        self.player = Player(screen, './resource/player.png')
        self.player.show()
        self.player.setDirection(0)

        # create enemy
        self.enemies = [
            Enemy(self.screen, './resource/enemy.png', random.randint(30, self.screen_H - 100), random.randint(0, 100)) \
            for i in range(10)]

        myChannel = mixer.Channel(1)
        myChannel.set_volume(0.5)
        backgroundMusic = random.randint(1, 3)
        if backgroundMusic == 1:
            myChannel.play(mixer.Sound("./resource/background.wav"), -1)
        elif backgroundMusic == 2:
            myChannel.play(mixer.Sound("./resource/BackgroundMusicInvaderHomeworld.mp3"), -1)
        else:
            myChannel.play(mixer.Sound("./resource/BackgroundMusic4Pluto.mp3"), -1)

        self.explosionChannel = mixer.Channel(2)
        self.explosionSound = mixer.Sound("./resource/explosion.wav")
        self.explosionChannel.set_volume(0.2)


    def getScore(self):
        return self.score_value

    def getGameState(self):
        return self.gameState

    def collisionCheck(self):
        # global gameState
        # global score_value
        for en in self.enemies:
            if en.getState() == "game over":
                self.gameState = "over"
                return
        for b in self.bullets:
            for en in self.enemies:
                x1, y1 = b.getPoint()
                x2, y2 = en.getPoint()
                distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
                if distance < 40:
                    b.setState("die")
                    en.setState("die")

        for b in self.enemyBullet:
            x1, y1 = b.getPoint()
            x2, y2 = self.player.getPoint()
            distance = ((x2 + 25 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
            if distance < 30:
                self.player.state = "die"
                self.gameState = "over"

    def animate(self):
        for enemy in self.enemies:
            enemy.animate()

    def enemyFire(self):
        for enemy in self.enemies:
            if math.fabs(enemy.X - self.player.X) < 50:
                self.enemyBullet.append(enemy.fire())
                # enemyFirePeriod = time.get_ticks()
                break

    def gameUpdate(self):
        self.player.move()
        self.player.show()
        # update enemies
        for enemy in self.enemies:
            if enemy.getState() == "die":
                self.explosionChannel.play(self.explosionSound)
                self.explosionSound.play()
                self.enemies.remove(enemy)
                self.enemies.append(Enemy(self.screen, './resource/enemy.png', random.randint(30, self.screen_H - 100), 120))
                if self.score_value % 10 == 0:
                    if len(self.enemies) > 9:
                        self.enemies.append(Enemy(self.screen, './resource/enemy.png', random.randint(30, self.screen_H - 100), 120))
                self.score_value += 1
                continue
            enemy.move()
            enemy.show()

        # update player bullets
        for bullet in self.bullets:
            if bullet.state == "die":
                 self.bullets.remove(bullet)
            else:
                bullet.move()
                bullet.show()
        # update enemies bullets
        for bullet in self.enemyBullet:
            if bullet.state == "die":
                self.enemyBullet.remove(bullet)
            else:
                bullet.move()
                bullet.show()

        self.collisionCheck()
