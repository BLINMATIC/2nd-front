##################################
# Made by BLINMATIC (Onur Çetin) #
# Version 1.0 INDEV 07-APR-2023  #
##################################

import pygame
import pages
import json

cfg = json.loads(open("settings.json", "r").read())

pygame.init()

if cfg["screen"]["fullscreen"] == 1:
    screen = pygame.display.set_mode((cfg["screen"]["width"], cfg["screen"]["height"]), pygame.FULLSCREEN)
elif cfg["screen"]["fullscreen"] == 0:
    screen = pygame.display.set_mode((cfg["screen"]["width"], cfg["screen"]["height"]))
elif cfg["screen"]["fullscreen"] == -1:
    screen = pygame.display.set_mode((cfg["screen"]["width"], cfg["screen"]["height"]), pygame.NOFRAME)

clock = pygame.time.Clock()

menu = pages.main_menu(screen)
tab = pages.top_tab(screen)

resume = True
while resume:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            resume = False
    screen.fill((255, 255, 255))
    menu.mainloop()
    tab.mainloop()
    
    pygame.display.update()