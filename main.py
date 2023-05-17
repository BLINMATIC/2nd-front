import pygame
from constant import *
from soldiers_tab import *

resume = True
st = SoldiersTab()
game = Game()
ending = Ending(0)


while resume:
    CLOCK.tick(SCREEN_REFRESH_RATE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            resume = False

    SCREEN.fill((255, 255, 255))
    ending = Ending(game.score)

    if game.score < 0 or game.score >= 32:
        ending.loop()
    else:
        game.loop()
        st.loop(game.score)


    pygame.display.update()