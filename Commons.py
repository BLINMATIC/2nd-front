import pygame
import pygame.gfxdraw


class Coords:
	def GetCenter(L1, L2):
		return L1 // 2 - L2 // 2
	
	def GetCenterRational(L1, R1):
		return Coords.GetCenter(L1, L1 // R1)
	
	def GetRational(L1, R1):
		return L1 // R1

class TextButton:
	def __init__(self, X, Y, Width, Height, Display, RGB, Text, Callback):
		self.X = X
		self.Y = Y
		self.Width = Width
		self.Height = Height

		self.Display = Display
		self.RGB = RGB

		self.Font = pygame.font.Font("Res/Ubuntu", self.Height - 5)
		self.Text = Text

		self.IsPressed = False
		self.Callback = Callback

	def Loop(self):
		MX, MY = pygame.mouse.get_pos()

		pygame.draw.rect(self.Display, self.RGB, (self.X, self.Y, self.Width, self.Height))
		self.Display.blit(self.Font.render(" " + self.Text, True, (240, 240, 240)), (self.X, self.Y))
		
		if self.X < MX < self.X + self.Width and self.Y < MY < self.Y + self.Height:
			if pygame.mouse.get_pressed(3)[0] == 1 and not self.IsPressed:
				self.IsPressed = True
				self.Callback()
			
			if pygame.mouse.get_pressed(3)[0] == 0:
				self.IsPressed = False
		else:
			pygame.gfxdraw.box(self.Display, pygame.Rect(self.X,self.Y,self.Width,self.Height), (120,120,120,120))