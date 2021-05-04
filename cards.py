import pygame
import random

import global_def as gd

class Card:
    def __init__(self, name, number = 0):
        self.image = pygame.image.load(rf".\karticky\{name}.png")
        self.number = number

    def draw_card(self, pos_x, pos_y): # all positions and sizes in percents
        card = self.image.convert_alpha()
        card = pygame.transform.smoothscale(card, (round(gd.display_width/5.8), round(gd.display_height/2.8))) # new image size
        gd.display.blit(card, (round((gd.display_width/100)*pos_x), round((gd.display_height/100)*pos_y)))

    def draw_extension_card(self, pos_x, pos_y):
        card = self.image.convert_alpha()
        card = pygame.transform.smoothscale(card, (round(gd.display_height/2.8), round(gd.display_width/5.8))) 
        gd.display.blit(card, (round((gd.display_width/100)*pos_x), round((gd.display_height/100)*pos_y)))

seasons = [Card('18', 8), 
           Card('19', 8),
           Card('20', 7),
           Card('21', 6)]       

forrest_rules_cards = [Card('26'), 
                       Card('27'), 
                       Card('28'),
                       Card('29')]

water_rules_cards = [Card('30'), 
                     Card('31'), 
                     Card('32'),
                     Card('33')]

house_rules_cards = [Card('34'), 
                     Card('35'), 
                     Card('36'),
                     Card('37')]

area_rules_cards = [Card('38'), 
                    Card('39'), 
                    Card('40'),
                    Card('41')]

rules_cards = [random.choice(forrest_rules_cards), 
               random.choice(house_rules_cards), 
               random.choice(water_rules_cards),
               random.choice(area_rules_cards)]

monster_cards = [Card('01'), 
                 Card('02'), 
                 Card('03'),
                 Card('04'),
                 Card('A01'), 
                 Card('A02'), 
                 Card('A03'),
                 Card('A04')]

complete_playing_cards = [Card('05'), 
                 Card('06'), 
                 Card('07', 1),
                 Card('08', 1),
                 Card('09', 1), 
                 Card('10', 1), 
                 Card('11', 2),
                 Card('12', 2),
                 Card('13', 2),
                 Card('14', 2), 
                 Card('15', 2), 
                 Card('16', 2),
                 Card('17')]

extension_cards = [Card('S1'), 
                 Card('S2'), 
                 Card('S3'),
                 Card('S4'),
                 Card('S5'), 
                 Card('S6'), 
                 Card('S7'),
                 Card('S8')]
    





