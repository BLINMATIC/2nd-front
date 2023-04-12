import pygame
import Commons
from Commons import Coords
import json
from Constants import Color


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
			self.Display, Color.ButtonColor1, "Tamam", lambda: self.HidePage())

		self.FullScreenOnButton = Commons.TextButton(self.Width - self.Surface.get_width(), 0,
			self.Surface.get_width(), Coords.GetRational(self.Height, 32), 
			self.Display, Color.ButtonColor1, "Tam Ekran", lambda: self.FullScreenModifier())
		
		self.WindowedScreenButton = Commons.TextButton(self.Width - self.Surface.get_width(), Coords.GetRational(self.Height, 32),
			self.Surface.get_width(), Coords.GetRational(self.Height, 32), 
			self.Display, Color.ButtonColor2, "Normal Ekran", lambda: self.WindowedModifier())
		
	def CheckForShowing(self):
		if self.Show:
			self.X = self.Width - self.Surface.get_width()
			self.Y = 0

		if not self.Show:
			self.X = self.Width * -1
			self.Y = self.Height * -1

	def HidePage(self):
		self.Show = False

	def FullScreenModifier(self):
		Tmp = json.loads(open("Settings.json", "r").read())
		Tmp["Fullscreen"] = True
		open("Settings.json", "w").write(json.dumps(Tmp))
	
	def WindowedModifier(self):
		Tmp = json.loads(open("Settings.json", "r").read())
		Tmp["Fullscreen"] = False
		open("Settings.json", "w").write(json.dumps(Tmp))

	def Loop(self):
		if self.Show:
			self.Display.blit(self.Surface, (self.X, self.Y))
			self.CheckForShowing()
			self.Surface.fill(Color.FGColor)
			
			# Draw the ok button
			self.OkButton.Loop()

			# Draw the settings buttons
			self.FullScreenOnButton.Loop()
			self.WindowedScreenButton.Loop()