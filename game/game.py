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

        self.turkey = pygame.image.load("resource/turkey-flag.png")
        self.greece = pygame.image.load("resource/greece-flag.png")

        self.turkey_points = 0
        self.greece_points = 25

        self.winner = 0

    def loop(self):
        if self.show:
            self.display.blit(self.surface, (0, 0))
            self.surface.fill((255, 255, 255))
            self.window_title.loop()

            self.surface.blit(self.turkey, (4, 25))
            self.surface.blit(self.greece, (self.width - 104, 25))

            for i in range(self.turkey_points):
                pygame.draw.ellipse(self.surface, (255, 0, 0), (104 + i * 50, 25, 50, 50))

            for i in range(self.greece_points):
                pygame.draw.ellipse(self.surface, (0, 0, 255), (self.width - 154 - i * 50, 25, 50, 50))


            try:
                self.questions[self.current_question].loop()

                if self.questions[self.current_question].correct and self.questions[self.current_question].next:
                    self.current_question += 1
                    self.turkey_points += 1
                    self.greece_points -= 1
                    pygame.time.delay(300)

                if not self.questions[self.current_question].correct and self.questions[self.current_question].next:
                    self.current_question += 1
                    self.greece_points += 1
                    self.turkey_points -= 1
                    pygame.time.delay(300)

                if self.greece_points < 0:
                    self.winner = 1
                    self.current_question = len(self.questions) + 5

                if self.greece_points > 35:
                    self.winner = 2
                    self.current_question = len(self.questions) + 5

            except:
                if self.winner == 0:
                    pass
                if self.winner == 1:
                    self.display.blit(pygame.font.Font("resource/ubuntu_mono.ttf", 50).render("Sonuç", True, (0, 0, 0)), (0, 75))
                    self.display.blit(pygame.font.Font("resource/ubuntu_mono.ttf", 50).render("Türkler Kazandı", True, (0, 0, 0)), (0, 125))
                if self.winner == 2:
                    self.display.blit(
                        pygame.font.Font("resource/ubuntu_mono.ttf", 50).render("Sonuç", True, (0, 0, 0)), (0, 75))
                    self.display.blit(pygame.font.Font("resource/ubuntu_mono.ttf", 50).render("Yunanlar Kazandı", True, (0, 0, 0)), (0, 125))


