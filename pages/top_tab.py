##################################
# Made by BLINMATIC (Onur Çetin) #
# Version 1.0 INDEV 07-APR-2023  #
##################################

import pygame
import common


class top_tab:
    def __init__(self, dest: pygame.Surface):
        self.dest = dest
        self.width = dest.get_width()
        self.height = dest.get_height() // 16 

        self.surface = pygame.Surface((self.width, self.height))

        self.font = pygame.font.Font("res/ubuntu.ttf", self.height)
        self.exit_button = pygame.transform.scale(pygame.image.load("res/exit.png"), (self.height, self.height))
        self.exit_button_hover = pygame.transform.scale(pygame.image.load("res/exit_hover.png"), (self.height, self.height))

        self.exit_button_is_pressed = False
        
        self.exit_button_class = common.Button(
            self.width - self.height, 
            0, 
            self.height, 
            self.height, 
            lambda: exit(), 
            lambda: self.surface.blit(self.exit_button, (self.width - self.height, 0)), 
            lambda: self.surface.blit(self.exit_button_hover, (self.width - self.height, 0)))
            

    def mainloop(self):
        self.dest.blit(self.surface, (0, 0))
        self.surface.fill((120, 120, 120))

        self.exit_button_class.mainloop()
        self.surface.blit(self.font.render("V1.0 INDEV", True, (250, 250, 250)), (0, 0))
        
        


        