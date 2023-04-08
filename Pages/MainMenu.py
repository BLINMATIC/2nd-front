import pygame
from Commons import *
from .AboutPage import AboutPage


class MainMenu:
	def __init__(self, dest: pygame.Surface):
		self.dest = dest
		self.width = dest.get_width()
		self.height = dest.get_height()

		self.resume = True

		self.PlayButton = TextButton(
				CenterPosPercent(self.width, 50), 
				CenterPosPercent(self.height, 10) - GetPercentage(self.height, 10), 
				50, 10, self.dest, GREEN, "OYNA", lambda: print(""))
		self.SettingsButton = TextButton(
				CenterPosPercent(self.width, 50), 
				CenterPosPercent(self.height, 10), 
				50, 10, self.dest, BLUE, "AYARLAR", lambda: print(""))
		self.ExitButton = TextButton(
				CenterPosPercent(self.width, 50), 
				CenterPosPercent(self.height, 10) + GetPercentage(self.height, 10), 
				50, 10, self.dest, RED, "ÇıK", lambda: exit(0))
		self.AboutButton = TextButton(
				CenterPosPercent(self.width, 50), 
				CenterPosPercent(self.height, 10) + GetPercentage(self.height, 10) * 2, 
				50, 10, self.dest, YELLOW, "HAKKıNDA", lambda: self.AboutButtonCommand())

		self.About = AboutPage(self.dest)

	def AboutButtonCommand(self):
		self.resume = False
		self.About.resume = True

	def loop(self):
		if self.resume:
			pygame.draw.rect(
				self.dest, FG,
				(
					CenterPosPercent(self.width, 55), 
					CenterPosPercent(self.height, 15) - GetPercentage(self.height, 10), 
					GetPercentage(self.width, 55), 
					GetPercentage(self.height, 10) * 4 + GetPercentage(self.height, 5)
				)
			)
			self.PlayButton.loop()
			self.SettingsButton.loop()
			self.ExitButton.loop()
			self.AboutButton.loop()
		

