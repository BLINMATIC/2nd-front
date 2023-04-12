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


class AboutTab:
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

		# The document turned into lines 
		self.Lines = [
			"CEPHE 2",
			"",
			"Orijinal Fikir: Derya Solkun",
			"Yazılımcı: BLINMATIC",
			"Bu proje hiçbir şekilde Ticari olarak kullanılamaz.",
			"Bu projenin sahibi tamamen Onur Çetin (BLINMATIC) dir."]

		# The license image
		self.License = pygame.transform.scale(pygame.image.load("Res/License"), (self.Surface.get_width(), self.Surface.get_width() // 4))
		
		# Exit button
		self.OkButton = Commons.TextButton(0, self.Height - Coords.GetRational(self.Height, 16),
			self.Surface.get_width(), Coords.GetRational(self.Height, 16), 
			self.Surface, Color.ButtonColor1, "Tamam", lambda: self.HidePage())

	def CheckForShowing(self):
		if self.Show:
			self.X = 0
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
			self.Surface.fill(Color.FGColor)

			# Draw every single line of the document
			for i in range(0, len(self.Lines)):
				self.Surface.blit(self.Font.render(self.Lines[i], True, Color.TextColor), (0, i * Coords.GetRational(self.Height, 64)))
			
			# Draw the ok button
			self.OkButton.Loop()

			# Draw the license
			self.Surface.blit(self.License, (0, self.Height - Coords.GetRational(self.Height, 16) - self.Surface.get_width() // 4))