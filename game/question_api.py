import pygame
import constant
import prefab


class Question:
    def __init__(self, display: pygame.Surface, question, ans1, ans2, ans3, ans4, correct_ans):
        self.display = display
        self.width = display.get_width()
        self.height = display.get_height()
        self.y = 96
        self.show = False

        self.question = question

        self.answer_1 = prefab.Button(self.display, [0, self.height - 80, self.width, 20], ans1, lambda: self.answer_command(1))
        self.answer_2 = prefab.Button(self.display, [0, self.height - 60, self.width, 20], ans2, lambda: self.answer_command(2))
        self.answer_3 = prefab.Button(self.display, [0, self.height - 40, self.width, 20], ans3, lambda: self.answer_command(3))
        self.answer_4 = prefab.Button(self.display, [0, self.height - 20, self.width, 20], ans4, lambda: self.answer_command(4))

        self.correct_answer = correct_ans
        self.correct = False
        self.next = False

        self.font = pygame.font.Font("resource/ubuntu_mono", 20)

    def answer_command(self, number):
        if number == self.correct_answer:
            self.correct_answer = True
            self.next = True
        else:
            self.correct_answer = False
            self.next = True

    def loop(self):
        for i in range(0, len(self.question.split("\n"))):
            self.display.blit(self.font.render(self.question.split("\n")[i], True, constant.color.black), (0, 96 + i * 20))

        self.answer_1.loop()
        self.answer_2.loop()
        self.answer_3.loop()
        self.answer_4.loop()
