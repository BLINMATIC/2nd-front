import pygame
import constant
import prefab


class AboutTab:
    def __init__(self, display: pygame.Surface):
        # Dimensions
        # The height has been set to 64 and the width has been reduced by 64 to accommodate
        # the menu tab
        self.width = display.get_width()
        self.height = display.get_height() - 64
        self.y = 64

        # Surfaces
        self.display = display
        self.surface = pygame.Surface((self.width, self.height))

        self.show = False

        # Buttons
        self.close_button = prefab.Button(self.display, [0, self.height + 44, self.width, 20], "Tamam", lambda: self.hide_tab())

        # Lines of the document
        self.document = [
            "Cephe 2",
            "Orijinal fikir: Derya Solkun",
            "Yazılımcı: BLINMATIC",
            "Ses Efektleri",
            "button_click: https://github.com/D-MKF1/707/blob/master/Sounds/click.wav",
            "button_hover: https://github.com/D-MKF1/707/blob/master/Sounds/click2.wav"
        ]

        # Font
        self.font = pygame.font.Font("resource/ubuntu_mono", 15)

    def show_tab(self):
        self.show = True

    def hide_tab(self):
        self.show = False

    def loop(self):
        if self.show:
            self.display.blit(self.surface, (0, self.y))
            self.surface.fill(constant.color.fg)

            self.close_button.loop()

            for i in range(0, len(self.document)):
                self.surface.blit(self.font.render(self.document[i], True, constant.color.text), (0, i * 15))