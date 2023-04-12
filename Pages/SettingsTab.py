import pygame
import Commons
from Commons import Coords


class SettingsTab:
	def __init__(self, Display: pygame.Surface):
		self.Display = Display

		# Get display dimensions
		self.Width = Display.get_width()
		self.Height = Display.get_height()

		# Define surface and position
		self.Surface = pygame.Surface((Coords.GetRational(self.Width, 4), self.Height))
		self.X = 0
		self.Y = 0

		self.Show = False
		self.Font = pygame.font.Font("Res/Ubuntu", Coords.GetRational(self.Height, 64))
		
		# Exit button
		self.OkButton = Commons.TextButton(self.Width - self.Surface.get_width(), self.Height - Coords.GetRational(self.Height, 16),
			self.Surface.get_width(), Coords.GetRational(self.Height, 16), 
			self.Display, (200, 200, 200), "Tamam", lambda: self.HidePage())

	def CheckForShowing(self):
		if self.Show:
			self.X = self.Width - self.Surface.get_width()
			self.Y = 0

		if not self.Show:
			self.X = self.Width * -1
			self.Y = self.Height * -1

	def HidePage(self):
		self.Show = False

	def Loop(self):
		if self.Show:
			self.Display.blit(self.Surface, (self.X, self.Y))
			self.CheckForShowing()
			self.Surface.fill((120, 120, 120))
			
			# Draw the ok button
			self.OkButton.Loop()
