import pygame
from constant import *
from page_ending import Ending
from page_game import Game


class SoldiersTab:
    def __init__(self):
        self.x = 0

    def loop(self, score):
        self.x = 0
        if 0 <= score <= 32:
            pygame.draw.rect(SCREEN, (score * 7, 0, (32 - score) * 7), (0, SCREEN_HEIGHT - 48, SCREEN_WIDTH, SCREEN_HEIGHT))

        # Draw the flags
        SCREEN.blit(IMAGE_TR, (0, SCREEN_HEIGHT - 32))
        SCREEN.blit(IMAGE_GR, (SCREEN_WIDTH - 64, SCREEN_HEIGHT - 32))

        x = (SCREEN_WIDTH - 128) // 32

        # Draw all Turkish Soldiers
        for i in range(score):
            SCREEN.blit(IMAGE_TURKISH_SOLDIER, (64 + i * x, SCREEN_HEIGHT - 32))

        # Draw all Greek Soldiers
        for i in range(32 - score):
            SCREEN.blit(IMAGE_GREEK_SOLDIER, (SCREEN_WIDTH - 96 - i * x, SCREEN_HEIGHT - 32))

        if score < 5:
            SCREEN.blit(IMAGE_LOWHP, (0, SCREEN_HEIGHT - 48))

