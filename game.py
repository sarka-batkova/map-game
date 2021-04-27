import pygame
import random

import global_def as gd
import cards as c


pygame.init()

gd.display.fill(gd.white)

coord = [200,400,600,800]
for i in coord:
    card = random.choice(c.Rules_cards)
    card.draw_card(i, 700)
    c.Rules_cards.remove(card)



c.message("Press n for next card", gd.black, 40, 20, 50)

pygame.display.update()

def gameLoop():
    pass


while True:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameLoop()






