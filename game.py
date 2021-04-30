import pygame
import random

import global_def as gd
import cards


pygame.init()

gd.display.fill(gd.white)

cards.draw_letter("A", 200, 450)
cards.draw_letter("B", 400, 450)
cards.draw_letter("C", 600, 450)
cards.draw_letter("D", 800, 450)

coord = [200, 400, 600, 800]
for i in coord:
    card = random.choice(cards.rules_cards)
    card.draw_card(i, 650)
    cards.rules_cards.remove(card)

coord = [400, 600, 800]
for i in coord:
    card = random.choice(cards.extension_cards)
    card.draw_card(i, 110)
    cards.extension_cards.remove(card)


cards.message("Press spacebar for new season", gd.black, 40, 20, 50)
cards.message("Press n for next card", gd.black, 40, 20, 80)


playing_cards = []

monster_cards = []
for a in range(4):
    monster_card = random.choice(cards.monster_cards)
    monster_cards.append(monster_card)
    cards.monster_cards.remove(monster_card)

played_monster_cards = []
    



i = -1


def Season(i):
    pass


while True:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    i+=1
                    cards.seasons[i].draw_card(200, 110)

                    playing_cards = cards.complete_playing_cards.copy()
                    for b in range(i+1):
                        if monster_cards[b] not in played_monster_cards: playing_cards.append(monster_cards[b]) 
                    random.shuffle(playing_cards)

                    sum = 0
                    y = 50
                    pygame.draw.rect(gd.display, gd.white, [1100, 50, 1500, 1500])

                if event.key == pygame.K_n and sum < cards.seasons[i].number:
                    random_card = random.choice(playing_cards)
                    random_card.draw_card(1100, y)
                    playing_cards.remove(random_card)
                    if random_card in monster_cards:
                        played_monster_cards.append(random_card)
                    
                    y += 70
                    sum += random_card.number
                    if sum >= cards.seasons[i].number:
                        cards.message("Last card!", gd.black, 40, 1140, 940)


                

    pygame.display.update()






