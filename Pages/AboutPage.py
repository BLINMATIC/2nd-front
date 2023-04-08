import pygame
from Commons import *

class AboutPage:
	def __init__(self, dest: pygame.Surface):
		self.dest = dest
		self.width = dest.get_width()
		self.height = dest.get_height()

		self.font = pygame.font.Font("res/ubuntu.ttf", GetPercentage(self.height, 4))
		self.text = """- HAKKINDA -
Proje Fikri: Derya Solkun
Proje Yazılımcısı: Onur Çetin (BLINMATIC)

Versiyon: v1.1indev
Kaynak Kodu: https://github.com/BLINMATIC/History-Project
Yazı Fonu: https://design.ubuntu.com/font
"""
		
		self.BackButton = TextButton(
			0, 
			self.height - GetPercentage(self.height, 10),
			self.width, 
			GetPercentage(self.height, 2),
			self.dest, RED, "Geri Git", lambda: self.BackButtonCommand()
		)
		self.resume = False
	
	def BackButtonCommand(self):
		self.resume = False

	def loop(self):
		if self.resume:
			for i in range(0, len(self.text.split("\n"))):
				self.dest.blit(self.font.render(self.text.split("\n")[i], True, (0, 0, 0)), (0, i * GetPercentage(self.height, 4)))
			
			self.dest.blit(pygame.image.load("res/license.png"), (self.width - 250, self.height - GetPercentage(self.height, 10) - 88))
			self.BackButton.loop()
