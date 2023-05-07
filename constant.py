import pygame
import pygame.gfxdraw

pygame.init()
pygame.mixer.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_REFRESH_RATE = 240

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
CLOCK = pygame.time.Clock()

FONT = pygame.font.Font("resource/bahnscrift.ttf", 32)

IMAGE_BUTTON = pygame.image.load("resource/button_single.png")

TEXT_GETREADY = FONT.render("Hazır Ol!", True, (0, 0, 0))

COLOR_BLACK = (0, 0, 0)


class Button:
    def __init__(self, x, y, width, height, callback):
        self.x, self.y, self.width, self.height = x, y, width, height
        self.callback = callback
        self.is_pressed = False

    def loop(self):
        mx, my = pygame.mouse.get_pos()

        if self.x < mx < self.x + self.width and self.y < my < self.y + self.height:
            if pygame.mouse.get_pressed(3)[0] == 1:
                if not self.is_pressed:
                    self.is_pressed = True
                    self.callback()
            else:
                self.is_pressed = False
        else:
            pygame.gfxdraw.box(SCREEN, (self.x, self.y, self.width, self.height), (120, 120, 120, 120))
            self.is_pressed = True


pygame.display.set_caption("2nd Front")
pygame.display.set_icon(pygame.image.load("resource/icon_small.png"))