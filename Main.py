import pygame
import Pages

pygame.init()

Screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
Clock = pygame.time.Clock()

MM = Pages.MainMenu(Screen)

Resume = True
while Resume:
	Clock.tick(60)

	for Event in pygame.event.get():
		if Event.type == pygame.QUIT:
			Resume = False
	Screen.fill((255, 255, 255))
	MM.Loop()
	pygame.display.update()