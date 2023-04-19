import pygame
import constant
import prefab
from .question_api import Question


class Game:
    def __init__(self, display: pygame.Surface):
        self.display = display
        self.width = display.get_width()

        self.font = pygame.font.Font("resource/ubuntu_mono", 32)
        self.questions = [
            Question(self.display, "Cevap: \nA", "A", "B", "C", "D", 1),
            Question(self.display, "Cevap: \nB", "A", "B", "C", "D", 2),
            Question(self.display, "Cevap: \nC", "A", "B", "C", "D", 3),
            Question(self.display, "Cevap: \nD", "A", "B", "C", "D", 4)
        ]
        self.current_question = 0

        self.show = False

    def show_game(self):
        self.show = True

    def hide_game(self):
        self.show = False

    def loop(self):
        if self.show:
            pygame.draw.rect(self.display, constant.color.fg, (0, 32, self.width, 70))
            self.display.blit(self.font.render("Yunanlar", True, constant.color.text), (0, 64))
            self.display.blit(pygame.transform.scale(constant.texture.tab_divider, (self.width, 6)), (0, 96))

            try:
                self.questions[self.current_question].loop()
                if self.questions[self.current_question].next:
                    if self.questions[self.current_question].correct_answer:
                        print("Correct")
                        self.current_question += 1
                        pygame.time.delay(1000)
                    else:
                        print("Wrong")
                        self.current_question += 1
                        pygame.time.delay(1000)
            except:
                pass



