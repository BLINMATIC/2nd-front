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
    SCREEN.blit(IMAGE_TR, (0, SCREEN_HEIGHT - 32))
    SCREEN.blit(IMAGE_GR, (SCREEN_WIDTH - 64, SCREEN_HEIGHT - 32))
    x = (SCREEN_WIDTH - 128) // 32
    for i in range(g.score):
        pygame.draw.ellipse(SCREEN, (255, 0, 0), (64 + i * x, SCREEN_HEIGHT - x, x, x))

    for i in range(32 - g.score):
        pygame.draw.ellipse(SCREEN, (0, 0, 255), (SCREEN_WIDTH - 96 - i * x, SCREEN_HEIGHT - x, x, x))
    pygame.display.update()