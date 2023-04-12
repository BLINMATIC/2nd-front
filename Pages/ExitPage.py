import pygame
import Commons
from Commons import Coords
from Constants import Color


##################
# EDITING CLOSED #
# Do not edit    #
# this file      #
# anymore.       #
##################


class ExitPage:
	def __init__(self, Display: pygame.Surface):
		self.Display = Display

		# Get display dimensions
		self.Width = Display.get_width()
		self.Height = Display.get_height()

		# Define surface and position
		self.Surface = pygame.Surface((self.Width, self.Height))
		self.X = 0
		self.Y = 0

		self.Show = False
		self.Font = pygame.font.Font("Res/Ubuntu", Coords.GetRational(self.Height, 15))

		# Exit message
		self.Text = self.Font.render("ALT+F4", True, Color.TextColor)

	def CheckForShowing(self):
		if self.Show:
			self.X = 0
			self.Y = 0

		if not self.Show:
			self.X = self.Width * -1
			self.Y = self.Height * -1

	def Loop(self):
		self.Display.blit(self.Surface, (self.X, self.Y))
		self.CheckForShowing()
		self.Surface.fill((255, 0, 0))

		# Draw message
		self.Surface.blit(self.Text, (Coords.GetCenter(self.Width, self.Text.get_width()), Coords.GetCenter(self.Height, self.Text.get_height())))

