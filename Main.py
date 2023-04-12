import pygame
import Pages
import json
from Constants import Color

Cfg = json.loads(open("Settings.json", "r").read())

pygame.init()

if Cfg["Fullscreen"]:
	Screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
else:
	Screen = pygame.display.set_mode((Cfg["ScreenWidth"], Cfg["ScreenHeight"]))


Clock = pygame.time.Clock()

MM = Pages.MainMenu(Screen)

Resume = True
while Resume:
	Clock.tick(60)

	for Event in pygame.event.get():
		if Event.type == pygame.QUIT:
			Resume = False
	Screen.fill(Color.BGColor)
	MM.Loop()
	pygame.display.update()