import pygame
from constant import *
from page_game import Game

resume = True
g = Game()
while resume:
    CLOCK.tick(SCREEN_REFRESH_RATE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            resume = False

    SCREEN.fill((255, 255, 255))
    g.loop()
    pygame.display.update()