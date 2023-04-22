import os
import pygame
import prefab


def get_questions(display: pygame.Surface):
    print(__name__, ">> Beginning to build the question list")

    questions_list = []
    replace_from = ["-c", "-g", "-i", "-o", "-s", "-u"]
    replace_to = ["ç", "ğ", "ı", "ö", "ş", "ü"]

    for i in os.listdir("question"):
        file = open("question/" + i, "r").read().split("tsugi-no-rain")

        for j in range(0, len(file)):
            for k in range(6):
                file[j] = file[j].replace(replace_from[k], replace_to[k])

        questions_list.append(prefab.Question(display, file[0], file[1], file[2], file[3], file[4], int(file[5])))
        print(__name__, ">> Added question", i)

    print(__name__, ">> Question list built")
    return questions_list