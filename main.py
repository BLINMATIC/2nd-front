import pygame
import game


pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.NOFRAME)
clock = pygame.time.Clock()

g = game.Game(screen)
resume = True
while resume:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            resume = False
    screen.fill((255, 255, 255))
    g.loop()
    pygame.display.update()
