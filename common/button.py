##################################
# Made by BLINMATIC (Onur Çetin) #
# Version 1.0 INDEV 07-APR-2023  #
##################################

import pygame


class Button:
    def __init__(self, x, y, width, height, on_click, on_standby, on_hover):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        self.on_click = on_click
        self.on_standby = on_standby
        self.on_hover = on_hover

        self.is_pressed = False
    
    def mainloop(self):
        mx, my = pygame.mouse.get_pos()


        if self.x < mx < self.x + self.width and self.y < my < self.y + self.height:
            self.on_hover()

            if pygame.mouse.get_pressed(3)[0] == 1:
                
                if self.is_pressed == False:
                    self.on_click()
                    self.is_pressed = True

            if pygame.mouse.get_pressed(3)[0] == 0:
                self.is_pressed = False
        else:
            self.on_standby()