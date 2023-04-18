import pygame
import pygame.gfxdraw
import constant


class Button:
    def __init__(self, display: pygame.Surface, rect: list, text: str, callback: any):
        # Dimensions
        self.x = rect[0]
        self.y = rect[1]
        self.width = rect[2]
        self.height = rect[3]

        # Surfaces
        self.display = display
        self.surface = pygame.Surface((self.width, self.height))

        # Text
        self.font = pygame.font.Font("resource/ubuntu_mono", self.height)
        self.text = self.font.render(text, True, constant.color.text)

        # Function to execute on click
        self.callback = callback

        # Click and hover limiter variables
        self.is_pressed = False
        self.is_hovering = False

    def loop(self):
        self.display.blit(self.surface, (self.x, self.y))
        self.surface.blit(pygame.transform.scale(constant.texture.button, (self.width, self.height)), (0, 0))
        self.surface.blit(self.text, (self.width // 2 - self.text.get_width() // 2, 0))

        mx, my = pygame.mouse.get_pos()

        # Check for if the mouse in on the button
        if self.x < mx < self.x + self.width and self.y < my < self.y + self.height:
            # Prevents the hover sound from playing multiple times
            if not self.is_hovering:
                self.is_hovering = True
                constant.audio.button_hover.play()

            # Key press detection
            if pygame.mouse.get_pressed(3)[0] == 1:
                # Prevents multiple clicks while holding
                if not self.is_pressed:
                    constant.audio.button_click.play()
                    self.is_pressed = True
                    self.callback()
            else:
                self.is_pressed = False
        else:
            self.is_hovering = False

            # The button shading to show that it is not being hovered on
            pygame.gfxdraw.box(self.surface, pygame.Rect(0,0,self.width,self.height), (50,50,50,50))