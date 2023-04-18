import pygame
import constant
import graphic_elements


pygame.mixer.init()
pygame.init()

if constant.config.full_screen:
    screen = pygame.display.set_mode((constant.config.width, constant.config.height), pygame.FULLSCREEN)
    pygame.display.set_caption("2. Cephe - Tam Ekran")
elif not constant.config.full_screen:
    screen = pygame.display.set_mode((constant.config.width, constant.config.height))
    pygame.display.set_caption("2. Cephe")
else:
    screen = pygame.display.set_mode((640, 480), pygame.FULLSCREEN)
    pygame.display.set_caption("2. Cephe - Uyumluluk Modu")

menu_tab = graphic_elements.MenuTab(screen)


resume = True
while resume:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            resume = False
    screen.fill(constant.color.bg)
    menu_tab.loop()
    pygame.display.update()