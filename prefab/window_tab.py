import pygame
from prefab.button import Button

class WindowTab:
    def __init__(self, display: pygame.Surface, page_show: bool, page_title: str):
        self.display = display
        self.show = page_show
        self.title = page_title
        self.width = display.get_width()
        self.height = display.get_height()
        self.text = pygame.font.Font("resource/ubuntu_mono.ttf", 25).render(self.title, True, (0, 0, 0))

        self.close_button = Button(self.display, self.width - 128, 0, 25, "Close", lambda: self.close_button_action())

    def close_button_action(self):
        self.show = False

    def loop(self):
        pygame.draw.rect(self.display, (240, 240, 240), (0, 0, self.width, 25))
        self.display.blit(self.text, (4, 0))
        self.close_button.loop()
        pygame.draw.line(self.display, (240, 240, 240), (0, 25), (0, self.height), 4)
        pygame.draw.line(self.display, (240, 240, 240), (self.width - 4, 25), (self.width - 4, self.height), 4)
        pygame.draw.line(self.display, (240, 240, 240), (0, self.height - 4), (self.width, self.height - 4), 4)