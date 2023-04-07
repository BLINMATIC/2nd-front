##################################
# Made by BLINMATIC (Onur Çetin) #
# Version 1.0 INDEV 07-APR-2023  #
##################################

import pygame
import common

class main_menu:
    def __init__(self, dest: pygame.Surface):
        self.dest = dest
        self.width = dest.get_width()
        self.height = dest.get_height()

        self.surface = pygame.Surface((self.width, self.height))
        self.font = pygame.font.Font("res/ubuntu.ttf", self.height // 20)

        self.play_button_init()
        self.settings_button_init()
        
    def play_button_init(self):
        x = self.width // 2 - self.width // 8
        y = self.height // 2 - self.height // 40
        width = self.width // 4
        height = self.height // 20

        self.play_button = common.Button(
            self.width // 2 - self.width // 8, 
            self.height // 2 - self.height // 40, 
            self.width // 4, 
            self.height // 20,
            lambda: print("soon"),
            lambda: pygame.draw.rect(self.surface, (0, 120, 0), (x, y, width, height)),
            lambda: pygame.draw.rect(self.surface, (0, 200, 0), (x, y, width, height))
            )
    
    def play_button_loop(self):
        x = self.width // 2 - self.width // 8
        y = self.height // 2 - self.height // 40
        width = self.width // 4
        height = self.height // 20

        self.play_button.mainloop()
        self.surface.blit(self.font.render("PLAY", True, (255, 255, 255)), (x, y, width, height))

    def settings_button_init(self):
        x = self.width // 2 - self.width // 8
        y = self.height // 2 + self.height // 40
        width = self.width // 4
        height = self.height // 20

        self.settings_button = common.Button(
            x, 
            y, 
            width, 
            height,
            lambda: print("settings"),
            lambda: pygame.draw.rect(self.surface, (0, 0, 120), (x, y, width, height)),
            lambda: pygame.draw.rect(self.surface, (0, 0, 200), (x, y, width, height)))
    
    def settings_button_mainloop(self):
        x = self.width // 2 - self.width // 8
        y = self.height // 2 + self.height // 40
        width = self.width // 4
        height = self.height // 20

        self.settings_button.mainloop()
        self.surface.blit(self.font.render("SETTINGS", True, (255, 255, 255)), (x, y, width, height))

    def mainloop(self):
        self.dest.blit(self.surface, (0, 0))
        self.surface.fill((255, 255, 255))
        self.play_button_loop()
        self.settings_button_mainloop()
        