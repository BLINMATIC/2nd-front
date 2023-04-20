import os
import pygame
import prefab


def get_questions(display: pygame.Surface):
    questions_list = []
    replace_from = ["-c", "-g", "-i", "-o", "-s", "-u"]
    replace_to = ["ç", "ğ", "ı", "ö", "ş", "ü"]

    for i in os.listdir("question"):
        file = open("question/" + i, "r").read().split("tsugi-no-rain")

        for i in range(0, len(file)):
            for j in range(6):
                file[i] = file[i].replace(replace_from[j], replace_to[j])

        questions_list.append(prefab.Question(display, file[0], file[1], file[2], file[3], file[4], int(file[5])))

    return questions_list