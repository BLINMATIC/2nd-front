import pygame
from Commons import *
from Pages import *


pygame.init()

screen = pygame.display.set_mode((1280, 720))

MainMenuPage = MainMenu(screen)

resume = True
while resume:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			resume = False
	screen.fill(BG)
	
	if MainMenuPage.resume:
		MainMenuPage.loop()
	elif MainMenuPage.About.resume:
		MainMenuPage.About.loop()
	
	if not MainMenuPage.About.resume:
		MainMenuPage.resume = True
	elif not MainMenuPage.resume:
		MainMenuPage.About.resume = True
		MainMenuPage.About.loop()
	pygame.display.update()