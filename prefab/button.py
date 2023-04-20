import pygame


class Button:
    def __init__(self, display: pygame.Surface, x, y, height, text, callback):
        self.display = display
        self.x = x
        self.y = y
        self.height = height

        self.font = pygame.font.Font("resource/ubuntu_mono.ttf", self.height)
        self.text_raw = text
        self.is_pressed = False

        self.draw_button((0, 0, 0))
        self.callback = callback

    def draw_button(self, color):
        self.text = self.font.render(self.text_raw, True, (0, 0, 0), color)
        pygame.draw.ellipse(self.display, color, (self.x + self.height // 2, self.y, self.height, self.height))
        pygame.draw.ellipse(self.display, color, (self.x + self.height // 2 + self.text.get_width(), self.y, self.height, self.height))
        self.display.blit(self.text, (self.x + self.height, self.y))

    def loop(self):
        mx, my = pygame.mouse.get_pos()
        if self.x < mx < self.x + self.height + self.text.get_width() and self.y < my < self.y + self.height:
            self.draw_button((200, 200, 200))
            if pygame.mouse.get_pressed(3)[0] == 1:
                if not self.is_pressed:
                    self.draw_button((150, 150, 150))
                    self.is_pressed = True
                    self.callback()
            else:
                self.draw_button((200, 200, 200))
                self.is_pressed = False
        else:
            self.draw_button((180, 180, 180))
