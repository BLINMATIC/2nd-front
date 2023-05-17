import pygame
from constant import *


class Ending:
    def __init__(self, score):
        self.score = score

        # Define the title text
        self.good_ending = FONT.render("TÜRKLER KAZANDI", True, (255, 0, 0))
        self.bad_ending = FONT.render("Yunanlar kazandı", True, (0, 0, 255))

    def loop(self):
        # Good ending (Turkish ending)
        if self.score >= 32:
            SCREEN.blit(self.good_ending, (SCREEN_WIDTH // 2 - self.good_ending.get_width() // 2, SCREEN_HEIGHT // 2))

        # Bad ending (Green Ending)
        if self.score < 0:
            SCREEN.blit(self.bad_ending, (SCREEN_WIDTH // 2 - self.bad_ending.get_width() // 2, SCREEN_HEIGHT // 2))