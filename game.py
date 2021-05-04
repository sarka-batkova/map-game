import pygame
import random

import global_def as gd
import cards


pygame.init()

gd.display.fill(gd.white)

gd.message("A", gd.red, 3, 11.03, 60)
gd.message("B", gd.red, 3, 28.97, 60)
gd.message("C", gd.red, 3, 46.90, 60)
gd.message("D", gd.red, 3, 64.83, 60)

coord = [3.44, 21.38, 39.31, 57.24]
for i in coord:
    card = random.choice(cards.rules_cards)
    card.draw_card(i, 64)
    cards.rules_cards.remove(card)

extension_cards = []
for a in range(3):
    extension_card = random.choice(cards.extension_cards)
    extension_cards.append(extension_card)
    cards.extension_cards.remove(extension_card)

extension_cards[0].draw_extension_card(22.76, 9)
extension_cards[1].draw_extension_card(47, 9)
extension_cards[2].draw_extension_card(34.48, 33)
    


gd.message("Press spacebar for new season", gd.black, 2.5, 1.38, 5)
gd.message("Press n for next card", gd.black, 2.5, 1.38, 8)


playing_cards = []

monster_cards = []
for a in range(4):
    monster_card = random.choice(cards.monster_cards)
    monster_cards.append(monster_card)
    cards.monster_cards.remove(monster_card)

played_monster_cards = []
    

i = -1
next_season_allowed = True


def Season(i):
    pass


while True:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and next_season_allowed:
                    next_season_allowed = False
                    i+=1
                    cards.seasons[i].draw_card(3.45, 13)

                    playing_cards = cards.complete_playing_cards.copy()
                    for b in range(i+1):
                        if monster_cards[b] not in played_monster_cards: playing_cards.append(monster_cards[b]) 
                    random.shuffle(playing_cards)

                    sum = 0
                    y = 3
                    pygame.draw.rect(gd.display, gd.white, [gd.display_width/100*79.31, gd.display_height/100*3, gd.display_width, gd.display_height])

                if event.key == pygame.K_n and playing_cards and sum < cards.seasons[i].number:
                    random_card = random.choice(playing_cards)
                    random_card.draw_card(79.31, y)
                    playing_cards.remove(random_card)
                    if random_card in monster_cards:
                        played_monster_cards.append(random_card)
                    
                    y += 7
                    sum += random_card.number
                    if sum >= cards.seasons[i].number:
                        gd.message("Last card!", gd.black, 3, 83, 95)
                        next_season_allowed = True


                

    pygame.display.update()






