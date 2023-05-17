import pygame
import pygame.gfxdraw

pygame.init()

SCREEN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

SCREEN_WIDTH = SCREEN.get_width()
SCREEN_HEIGHT = SCREEN.get_height()
SCREEN_REFRESH_RATE = 240

CLOCK = pygame.time.Clock()

FONT = pygame.font.Font("resource/bahnscrift.ttf", 32)
TEXT_GETREADY = FONT.render("Hazır Ol!", True, (0, 0, 0))

COLOR_BLACK = (0, 0, 0)

IMAGE_TR = pygame.image.load("resource/flag_tr.png")
IMAGE_GR = pygame.image.load("resource/flag_gr.png")
IMAGE_GREEK_SOLDIER = pygame.image.load("resource/soldier_greece.png")
IMAGE_TURKISH_SOLDIER = pygame.image.load("resource/soldier_turkey.png")
IMAGE_LOWHP = pygame.image.load("resource/turkey_lowhp.png")


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