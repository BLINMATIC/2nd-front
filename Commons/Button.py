import pygame
from .Coords import *
import pygame.gfxdraw
from .Colours import *


class TextButton:
	def __init__(self, x: int, y: int, width: int, height: int, dest: pygame.Surface, rgb: tuple, text: str, callback):
		self.dest = dest

		# Display Dimensions
		self.width = dest.get_width()
		self.height = dest.get_height()

		# Position
		self.x = x
		self.y = y
		# Dimensions As Percentage
		self.width = GetPercentage(self.width, width)
		self.height = GetPercentage(self.height, height)

		self.is_pressed = False

		self.rgb = rgb
		self.font = pygame.font.Font("res/ubuntu.ttf", self.height)
		self.text = text.capitalize()

		# Function to execute on button press
		self.callback = callback

	def loop(self):
		mx, my = pygame.mouse.get_pos()

		# Draw Button and text
		pygame.draw.rect(self.dest, self.rgb, (self.x, self.y, self.width, self.height))
		self.dest.blit(self.font.render(self.text, True, BG), (self.x, self.y))

		if self.x < mx < self.x + self.width and self.y < my < self.y + self.height:
			if pygame.mouse.get_pressed(3)[0] == 1 and not self.is_pressed:
				self.is_pressed = True
				self.callback()
			if pygame.mouse.get_pressed(3)[0] == 0:
				self.is_pressed == False
		else:
			# Shading
			pygame.gfxdraw.box(self.dest, pygame.Rect(self.x,self.y, self.width, self.height), (120, 120, 120, 120))