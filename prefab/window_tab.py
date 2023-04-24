import pygame
from prefab.button import Button


class WindowTab:
    def __init__(self, display: pygame.Surface, page_show: bool, page_title: str):
        self.display = display
        self.show = page_show
        self.title = page_title
        self.width = display.get_width()
        self.height = display.get_height()
        self.font = pygame.font.Font("resource/ubuntu_mono.ttf", 25)
        self.text_object = self.font.render(self.title, True, (0, 0, 0))

    def close_button_action(self):
        self.show = False

    def loop(self):
        self.text_object = self.font.render(self.title, True, (0, 0, 0))
        pygame.draw.rect(self.display, (240, 240, 240), (0, 0, self.width, 25))

        self.display.blit(self.text_object, (4, 0))