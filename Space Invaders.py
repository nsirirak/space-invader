# 1/26/2022 (Finish Date) Dad, Colin
import sys

import pygame
from Player import Player
from Enemy import Enemy
from pygame import mixer,time
import random
import math
from GameControl import GameControl

# Initialize the game
pygame.init()
# Create Screen
screen_H = 800
screen_V = 600
screen = pygame.display.set_mode((screen_H, screen_V))
background = pygame.image.load('./resource/Background.jpg')


# init clock
clock = time.Clock()
period = time.get_ticks()
enemyFirePeriod = time.get_ticks()

#Caption and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('./resource/ufo.png')
pygame.display.set_icon(icon)

UPDATE_GAME = pygame.USEREVENT + 1
ANIMATE = pygame.USEREVENT + 2

textX = 10
textY = 10
font = pygame.font.Font('freesansbold.ttf', 24)

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)

# create custom event that fire every 16 ms
time.set_timer(UPDATE_GAME, 16)

time.set_timer(ANIMATE, 300)

enemy_fire_time = random.randint(500, 1000)
bgX = random.randint(-250, 0)
game_over = "no"

control = GameControl(screen)


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def show_score(x, y):
    score = font.render(f"Score : {control.getScore()}", True, (255, 255, 255))
    if game_over == "no":
        screen.blit(score, (x, y))
    else:
        screen.blit(score, (350, 325))
# Game Loop
running = True
while running:
    #screen.fill((0, 0, 0))  black background
    screen.blit(background, (bgX, 0))
    show_score(textX, textY)
    for event in pygame.event.get():
        # animate enemies every 300 ms
        if event.type == ANIMATE:
            control.animate()
        # update game every 1/60 second
        if event.type == UPDATE_GAME:
            control.gameUpdate()
            pygame.display.update()
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                control.player.setDirection(-1)
            if event.key == pygame.K_RIGHT:
                control.player.setDirection(1)
            if event.key == pygame.K_SPACE:
                if time.get_ticks() - period > 300:
                    control.bullets.append(control.player.fire())
                    period = time.get_ticks()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                control.player.setDirection(0)

    # enemies fire a bullet
    if time.get_ticks() - enemyFirePeriod > enemy_fire_time:
        enemy_fire_time = random.randint(500, 1500)
        control.enemyFire()
        enemyFirePeriod = time.get_ticks()

    if control.gameState == "over":
        mixer.stop()
        for e in control.enemies:
            e.Y = 1000
        pygame.event.set_blocked(UPDATE_GAME)
        game_over_text()
        game_over = "yes"
        pygame.display.update()

#pygame.quit()
#sys.exit()
