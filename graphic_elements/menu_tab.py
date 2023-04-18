import pygame
import constant
import prefab
from .about_tab import AboutTab
from .settings_tab import SettingsTab


class MenuTab:
    def __init__(self, display: pygame.Surface):
        # Dimensions
        self.width = display.get_width()
        self.height = 64
        self.y = 0

        self.display = display
        self.surface = pygame.Surface((self.width, self.height))

        self.show = True

        # Define pages
        self.about_tab = AboutTab(self.display)
        self.settings_tab = SettingsTab(self.display)

        # Buttons
        self.play_button = prefab.Button(self.surface, [0, 10, 150, 20], "Oyna", lambda: print())
        self.settings_button = prefab.Button(self.surface, [150, 10, 150, 20], "Ayarlar", lambda: self.settings_tab.show_tab())
        self.about_button = prefab.Button(self.surface, [300, 10, 150, 20], "Hakkında", lambda: self.about_tab.show_tab())
        self.exit_button = prefab.Button(self.surface, [450, 10, 150, 20], "Çıkış", lambda: exit(0))

    def loop(self):
        self.about_tab.loop()
        self.settings_tab.loop()

        if self.show:
            self.display.blit(self.surface, (0, self.y))
            self.surface.fill(constant.color.gray)

            # Show and activate the buttons
            self.play_button.loop()
            self.settings_button.loop()
            self.about_button.loop()
            self.exit_button.loop()

            # Draw the menu divisor
            self.surface.blit(pygame.transform.scale(constant.texture.tab_divider, (self.width, 6)), (0, 58))