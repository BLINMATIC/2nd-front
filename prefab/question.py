import pygame
import prefab


class Question:
    def __init__(self, display: pygame.Surface, title: str, ans1: str, ans2: str, ans3: str, ans4: str, correct_ans: int):
        self.display = display
        self.width = display.get_width()
        self.height = display.get_height()

        self.ans1 = prefab.Button(self.display, 4, self.height - 84, 20, ans1, lambda: self.answer(1))
        self.ans2 = prefab.Button(self.display, 4, self.height - 64, 20, ans2, lambda: self.answer(2))
        self.ans3 = prefab.Button(self.display, 4, self.height - 44, 20, ans3, lambda: self.answer(3))
        self.ans4 = prefab.Button(self.display, 4, self.height - 24, 20, ans4, lambda: self.answer(4))

        self.title = title.split("\n")

        self.next = False
        self.correct = False

        self.correct_answer = correct_ans

    def answer(self, id):
        if id == self.correct_answer:
            self.correct = True
            self.next = True
        else:
            self.correct = False
            self.next = True

    def loop(self):
        self.ans1.loop()
        self.ans2.loop()
        self.ans3.loop()
        self.ans4.loop()

        for i in range(0, len(self.title)):
            self.display.blit(pygame.font.Font("resource/ubuntu_mono.ttf", 25).render(self.title[i], True, (0, 0, 0)), (4, 25 + i * 25))