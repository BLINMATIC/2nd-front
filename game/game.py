import pygame
import prefab
from .get_questions import get_questions


class Game:
    def __init__(self, display: pygame.Surface):
        self.display = display
        self.width = display.get_width()
        self.height = display.get_height()
        self.show = True
        self.surface = pygame.Surface((self.width, self.height))

        self.window_title = prefab.WindowTab(self.surface, self.show, "Game")

        self.questions = get_questions(self.surface)

        self.current_question = 0

    def loop(self):
        if self.show:
            self.display.blit(self.surface, (0, 0))
            self.surface.fill((255, 255, 255))
            self.window_title.loop()

            try:
                self.questions[self.current_question].loop()

                if self.questions[self.current_question].correct and self.questions[self.current_question].next:
                    self.current_question += 1
                    pygame.time.delay(300)

                if not self.questions[self.current_question].correct and self.questions[self.current_question].next:
                    self.current_question += 1
                    pygame.time.delay(300)
            except:
                pass


