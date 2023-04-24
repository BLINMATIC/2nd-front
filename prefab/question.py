import pygame
import prefab

pygame.mixer.init()


class Question:
    def __init__(self, display: pygame.Surface, title: str, ans1: str, ans2: str, ans3: str, ans4: str, correct_ans: int):
        self.display = display
        self.width = display.get_width()
        self.height = display.get_height()

        self.ans1 = prefab.Button(self.display, 4, self.height - 164, 40, ans1, lambda: self.answer(1))
        self.ans2 = prefab.Button(self.display, 4, self.height - 124, 40, ans2, lambda: self.answer(2))
        self.ans3 = prefab.Button(self.display, 4, self.height - 84, 40, ans3, lambda: self.answer(3))
        self.ans4 = prefab.Button(self.display, 4, self.height - 44, 40, ans4, lambda: self.answer(4))

        self.title = title.split("\n")

        self.next = False
        self.correct = False

        self.correct_answer = correct_ans

        self.correct_answer_audio = pygame.mixer.Sound("resource/correct.wav")
        self.wrong_answer_audio = pygame.mixer.Sound("resource/wrong.wav")
        self.answer_audio_played = False

    def answer(self, id):
        if id == self.correct_answer:
            self.correct = True
            self.next = True

            if not self.answer_audio_played:
                self.correct_answer_audio.play()
                self.answer_audio_played = True
        else:
            self.correct = False
            self.next = True

            if not self.answer_audio_played:
                self.wrong_answer_audio.play()
                self.answer_audio_played = True

    def loop(self):
        self.ans1.loop()
        self.ans2.loop()
        self.ans3.loop()
        self.ans4.loop()

        for i in range(0, len(self.title)):
            self.display.blit(pygame.font.Font("resource/ubuntu_mono.ttf", 50).render(self.title[i], True, (0, 0, 0)), (4, 75 + (self.width // 35) + i * 50))