import pygame
import Commons
from Commons import Coords

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
			self.Surface, (150, 150, 150), "Ayarlar", lambda: print(""))
		
		self.AboutButton = Commons.TextButton(
			Coords.GetCenterRational(self.Width, 3), Coords.GetCenterRational(self.Height, 10) + Coords.GetRational(self.Height, 5),
			Coords.GetRational(self.Width, 3), Coords.GetRational(self.Height, 10),
			self.Surface, (200, 200, 200), "Hakkında", lambda: self.AboutButtonCommand())

		self.ExitButton = Commons.TextButton(
			Coords.GetCenterRational(self.Width, 3), Coords.GetCenterRational(self.Height, 10) + Coords.GetRational(self.Height, 10) * 3,
			Coords.GetRational(self.Width, 3), Coords.GetRational(self.Height, 10),
			self.Surface, (150, 150, 150), "Çık", lambda: self.ExitButtonCommand())
		
		self.ExitPage = ExitPage(self.Surface)
		self.AboutPage = About(self.Surface)

	def CheckForShowing(self):
		if self.Show:
			self.X = 0
			self.Y = 0

		if not self.Show:
			self.X = self.Width * -1
			self.Y = self.Height * -1

	def ExitButtonCommand(self):
		self.AboutPage.Show = False
		self.ExitPage.Show = True

	def AboutButtonCommand(self):
		self.AboutPage.Show = True

	def Loop(self):
		self.ExitPage.Loop()
		self.AboutPage.Loop()

		self.Display.blit(self.Surface, (self.X, self.Y))
		self.CheckForShowing()
		self.Surface.fill((255, 255, 255))

		self.PlayButton.Loop()
		self.SettingsButton.Loop()
		self.AboutButton.Loop()
		self.ExitButton.Loop()


class ExitPage:
	def __init__(self, Display: pygame.Surface):
		self.Display = Display
		self.Width = Display.get_width()
		self.Height = Display.get_height()

		self.Surface = pygame.Surface((self.Width, self.Height))
		self.X = 0
		self.Y = 0

		self.Show = False
		self.Font = pygame.font.Font("Res/Ubuntu", Coords.GetRational(self.Height, 15))

		self.Text = self.Font.render("It is safe to press ALT+F4 or ^C", True, (255, 255, 255))
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
		self.Surface.blit(self.Text, (Coords.GetCenter(self.Width, self.Text.get_width()), Coords.GetCenter(self.Height, self.Text.get_height())))


class About:
	def __init__(self, Display: pygame.Surface):
		self.Display = Display
		self.Width = Display.get_width()
		self.Height = Display.get_height()

		self.Surface = pygame.Surface((Coords.GetRational(self.Width, 4), self.Height))
		self.X = 0
		self.Y = 0

		self.Show = False
		self.Font = pygame.font.Font("Res/Ubuntu", Coords.GetRational(self.Height, 64))

		self.Lines = [
			"CEPHE 2",
			"######",
			"Orijinal Fikir: Derya Solkun",
			"Yazılımcı: BLINMATIC",
			"Bu proje hiçbir şekilde Ticari olarak kullanılamaz.",
			"Bu projenin sahibi tamamen Onur Çetin (BLINMATIC) dir.",
			"",
			"Это произведение доступно по лицензии Creative Commons",
			"«Attribution-NonCommercial-NoDerivatives»",
			"(«Атрибуция-Некоммерчески-БезПроизводных») 4.0 Всемирная.",
			""
		]
		self.License = pygame.transform.scale(pygame.image.load("Res/License"), (self.Surface.get_width(), Coords.GetRational(self.Height, 16)))
		self.OkSign = Commons.TextButton(0, self.Height - Coords.GetRational(self.Height, 16),
			self.Surface.get_width(), Coords.GetRational(self.Height, 16), 
			self.Surface, (200, 200, 200), "Tamam", lambda: self.HidePage())

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
		self.Display.blit(self.Surface, (self.X, self.Y))
		self.CheckForShowing()
		self.Surface.fill((120, 120, 120))

		for i in range(0, len(self.Lines)):
			self.Surface.blit(self.Font.render(self.Lines[i], True, (255, 255, 255)), (0, i * Coords.GetRational(self.Height, 64)))
		
		self.OkSign.Loop()
		self.Surface.blit(self.License, (0, self.Height - Coords.GetRational(self.Height, 16) * 2))