import sysconfig
import pygame
import game


pygame.init()
print(__name__, ">> Running Python version " + sysconfig.get_python_version())
print(__name__, ">> Pygame initialised")


screen = pygame.display.set_mode((0, 0), pygame.NOFRAME)
print(__name__, ">> Screen initialised as full-screen")
clock = pygame.time.Clock()
print(__name__, ">> Clock initialised")

g = game.Game(screen)
print(__name__, "Game window initialised")
resume = True
while resume:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            resume = False
    screen.fill((255, 255, 255))
    g.loop()
    pygame.display.update()
