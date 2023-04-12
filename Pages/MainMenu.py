import pygame
import Commons
from Commons import Coords
from Pages.AboutTab import AboutTab
from Pages.ExitPage import ExitPage
from Pages.SettingsTab import SettingsTab


##################
# EDITING CLOSED #
# Do not edit    #
# this file      #
# anymore.       #
##################
# Except:        #
# Line: 34,7     #
##################


class MainMenu:
	def __init__(self, Display: pygame.Surface):
		self.Display = Display
		self.Width = Display.get_width()
		self.Height = Display.get_height()

		self.Surface = pygame.Surface((self.Width, self.Height))
		self.X = 0
		self.Y = 0

		self.Show = True

		self.PlayButton = Commons.TextButton(
			Coords.GetCenterRational(self.Width, 3), Coords.GetCenterRational(self.Height, 10),
			Coords.GetRational(self.Width, 3), Coords.GetRational(self.Height, 10),
			self.Surface, (200, 200, 200), "Oyna", lambda: print(""))
		
		self.SettingsButton = Commons.TextButton(
			Coords.GetCenterRational(self.Width, 3), Coords.GetCenterRational(self.Height, 10) + Coords.GetRational(self.Height, 10),
			Coords.GetRational(self.Width, 3), Coords.GetRational(self.Height, 10),
			self.Surface, (150, 150, 150), "Ayarlar", lambda: self.SettingsButtonCommand())
		
		self.AboutButton = Commons.TextButton(
			Coords.GetCenterRational(self.Width, 3), Coords.GetCenterRational(self.Height, 10) + Coords.GetRational(self.Height, 5),
			Coords.GetRational(self.Width, 3), Coords.GetRational(self.Height, 10),
			self.Surface, (200, 200, 200), "Hakkında", lambda: self.AboutButtonCommand())

		self.ExitButton = Commons.TextButton(
			Coords.GetCenterRational(self.Width, 3), Coords.GetCenterRational(self.Height, 10) + Coords.GetRational(self.Height, 10) * 3,
			Coords.GetRational(self.Width, 3), Coords.GetRational(self.Height, 10),
			self.Surface, (150, 150, 150), "Çık", lambda: self.ExitButtonCommand())
		
		self.ExitPage = ExitPage(self.Display)
		self.AboutTab = AboutTab(self.Surface)
		self.SettingsTab = SettingsTab(self.Surface)

	def CheckForShowing(self):
		if self.Show:
			self.X = 0
			self.Y = 0

		if not self.Show:
			self.X = self.Width * -1
			self.Y = self.Height * -1

	def ExitButtonCommand(self):
		self.Show = False
		self.AboutTab.Show = False
		self.ExitPage.Show = True

	def AboutButtonCommand(self):
		self.AboutTab.Show = True

	def SettingsButtonCommand(self):
		self.SettingsTab.Show = True

	def Loop(self):
		self.ExitPage.Loop()
		self.AboutTab.Loop()
		self.SettingsTab.Loop()

		if self.Show:
			self.Display.blit(self.Surface, (self.X, self.Y))
			self.CheckForShowing()
			self.Surface.fill((255, 255, 255))

			self.PlayButton.Loop()
			self.SettingsButton.Loop()
			self.AboutButton.Loop()
			self.ExitButton.Loop()