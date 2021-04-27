import pygame
import random

import global_def as gd
import cards as c


pygame.init()

gd.display.fill(gd.white)

c.draw_letter("A", 200, 450)
c.draw_letter("B", 400, 450)
c.draw_letter("C", 600, 450)
c.draw_letter("D", 800, 450)

coord = [200,400,600,800]
for i in coord:
    card = random.choice(c.Rules_cards)
    card.draw_card(i, 650)
    c.Rules_cards.remove(card)

c.message("Press spacebar for new season", gd.black, 40, 20, 50)
c.message("Press n for next card", gd.black, 40, 20, 80)

i = 0

def Season(i):
    c.Seasons[i].draw_card(200, 110)
    monster = random.choice(c.Monster_cards)
    c.Playing_cards.append(monster)
    random.shuffle(c.Playing_cards)


while True:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Season(i)
                    i+=1
                if event.key == pygame.K_n:
                    random_card = random.choice(c.Playing_cards)
                    random_card.draw_card(1100, 200)
                    c.Playing_cards.remove(random_card)

    pygame.display.update()






