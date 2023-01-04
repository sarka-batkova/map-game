"""Module for the game itself.

Methods:
    init(): Inicializaiton of the game.
    main(): The game.
"""

import pygame
import random
import global_def as gd
import cards

def init():
    """Inicialization of the game."""
    pygame.init()
    gd.display.fill(gd.white)

    gd.message("A", gd.red, 3, 11.03, 60)
    gd.message("B", gd.red, 3, 28.97, 60)
    gd.message("C", gd.red, 3, 46.90, 60)
    gd.message("D", gd.red, 3, 64.83, 60)
    gd.message("Press spacebar for new season", gd.black, 2.5, 1.38, 5)
    gd.message("Press n for next card", gd.black, 2.5, 1.38, 8)

    # drawing of rules cards
    random.shuffle(cards.rules_cards)
    rules_cards_coord = [3.44, 21.38, 39.31, 57.24]
    for i, coord in enumerate(rules_cards_coord):
        cards.rules_cards[i].draw_card(coord, 64)

    # drawing of extension cards
    extension_cards = random.sample(cards.extension_cards, 3)
    extension_cards[0].draw_card(22.76, 9, "ext")
    extension_cards[1].draw_card(47, 9, "ext")
    extension_cards[2].draw_card(34.48, 33, "ext")



def main():
    """The game."""
    init()

    frame_coord = [3.3, 21.3, 39.2, 57.2, 3.3, 100]
    playing_cards = []
    monster_cards = random.sample(cards.monster_cards, 4)
    played_monster_cards = []
    i = -1 # keeps track of current season
    next_season_allowed = True

    while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_SPACE and next_season_allowed: # new season
                next_season_allowed = False
                i+=1 # keeps track of current season
                sum = 0 # sum of card values
                y = 3 # pos_y of the first playing card
                cards.seasons[i].draw_card(3.45, 13) # draws season card

                # preparation of playing cards deck
                playing_cards = cards.complete_playing_cards.copy()
                for b in range(i+1):
                    if monster_cards[b] not in played_monster_cards: playing_cards.append(monster_cards[b]) 
                random.shuffle(playing_cards)
                
                # drawing of rectangles
                gd.rect(gd.white, 79, 0, gd.display_width, gd.display_height) # draws over playing cards from last turn
                gd.rect(gd.black, frame_coord[i], 59, 25, 41, 0.5) 
                gd.rect(gd.black, frame_coord[i+1], 59, 25, 41, 0.5)
                gd.rect(gd.white, frame_coord[i-1], 59, 25, 41, 0.5) # draws over first rectangle from last turn
                if i > 1:
                    gd.line(gd.black, frame_coord[i-1], 59, frame_coord[i-1]+17, 100, 1)
                    
            if event.key == pygame.K_n and playing_cards and sum < cards.seasons[i].number: # new card
                random_card = random.choice(playing_cards)
                random_card.draw_card(79.31, y)
                playing_cards.remove(random_card)
                if random_card in monster_cards:
                    played_monster_cards.append(random_card)
                
                y += 7 # new pos_y of the next playing card
                sum += random_card.number
                if sum >= cards.seasons[i].number:
                    gd.message("Last card!", gd.black, 3, 83, 95)
                    next_season_allowed = True

        pygame.display.update()

if __name__ == "__main__":
    main()





