import pygame
import prefab
from .get_questions import get_questions


class Game:
    def __init__(self, display: pygame.Surface):
        # Define dimensions
        self.width = display.get_width()
        self.height = display.get_height()

        self.show = True

        # Define surfaces
        self.display = display
        print(__name__, "Surfaces (1/3) >> self.display initialised")
        self.surface = pygame.Surface((self.width, self.height))
        print(__name__, "Surfaces (2/3) >> self.surface initialised")
        self.window_title = prefab.WindowTab(self.surface, self.show, "Game")
        print(__name__, "Surfaces (3/3) >> self.window_title initialised")

        # Build the questions list
        self.questions = get_questions(self.surface)
        self.current_question = 0

        # Flag images
        self.turkey = pygame.image.load("resource/turkey-flag.png")
        self.greece = pygame.image.load("resource/greece-flag.png")

        # Soldier count
        self.turkey_points = 1
        self.greece_points = 34

        # Winner indicator
        # ID | STATE
        # ---+------
        # 0  | Draw
        # 1  | Turkey
        # 2  | Greece
        self.winner = 0

        self.font = pygame.font.Font("resource/ubuntu_mono.ttf", 50)

        self.turkey_point_number = self.font.render(str(self.turkey_points), True, (0, 0, 0))
        self.greece_point_number = self.font.render(str(self.greece_points), True, (0, 0, 0))

    def results_screen(self):
        self.window_title.title = "Game"
        self.window_title.loop()

        if self.winner == 0:
            text = self.font.render("Beraberlik", True, (0, 0, 0))
            self.display.blit(text, (self.width // 2 - text.get_width() // 2, 125))

        if self.winner == 1:
            text = self.font.render("Türkler Kazandı", True, (0, 0, 0))
            self.display.blit(text, (self.width // 2 - text.get_width() // 2, 125))

        if self.winner == 2:
            text = self.font.render("Yunanlar Kazandı", True, (0, 0, 0))
            self.display.blit(text, (self.width // 2 - text.get_width() // 2, 125))

    def draw(self):
        self.turkey_point_number = self.font.render(str(self.turkey_points), True, (0, 0, 0))
        self.greece_point_number = self.font.render(str(self.greece_points), True, (0, 0, 0))

        if self.show:
            self.display.blit(self.surface, (0, 0))
            self.surface.fill((255, 255, 255))
            pygame.draw.rect(self.surface, (240, 240, 240), (100, 25, self.width - 200, 50))

            # Draw the flags
            self.surface.blit(self.turkey, (0, 25))
            self.surface.blit(self.greece, (self.width - 100, 25))

            # Draw the points in numbers
            self.surface.blit(self.turkey_point_number, (100, 25))
            self.surface.blit(self.greece_point_number, (self.width - 100 - self.greece_point_number.get_width(), 25))

            # Draw the Turkish soldiers (flag length + 50number)
            for i in range(self.turkey_points):
                pygame.draw.ellipse(self.surface, (255, 0, 0), (i * self.width // 35, 75, self.width // 35, self.width // 35))

            # Draw the Greek soldiers (surface width - flag length - 50number)
            for i in range(self.greece_points):
                pygame.draw.ellipse(self.surface, (0, 0, 255), (self.width - i * self.width // 35, 75, self.width // 35, self.width // 35))

    def loop(self):
        self.draw()
        try:
            # Draws the current question
            self.questions[self.current_question].loop()

            # Detects for correct question
            if self.questions[self.current_question].correct and self.questions[self.current_question].next:
                self.current_question += 1
                self.turkey_points += 1
                self.greece_points -= 1
                print(__name__, ">> Question correct")
                pygame.time.delay(300)

            # Detects for wrong question
            if not self.questions[self.current_question].correct and self.questions[self.current_question].next:
                self.current_question += 1
                self.greece_points += 1
                self.turkey_points -= 1
                print(__name__, ">> Question wrong")
                pygame.time.delay(300)

            # Makes Turkey win if all Greek soldiers are defeated
            if self.greece_points < 0:
                self.winner = 1
                self.current_question = len(self.questions) + 5

            # Makes Greece win if all Turkish soldiers are defeated
            if self.greece_points > 35:
                self.winner = 2
                self.current_question = len(self.questions) + 5

            # Sets the window title to Question + question number
            self.window_title.title = "Soru " + str(self.current_question)
            self.window_title.loop()

            # NOTE
            # Draw happens when the game runs out of questions

        except:
            self.results_screen()


