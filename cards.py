import pygame
import random

import global_def as gd


def message(msg, color, font_size, x, y):
    gd.display.blit(pygame.font.SysFont(None, font_size).render(msg, True, color), [x, y])

def draw_letter(letter, pos_x, pos_y):
    pygame.draw.rect(gd.display, gd.black, [pos_x, pos_y, 200, 150], 10)
    message(letter, gd.red, 100, pos_x + 75, pos_y + 55)

class Card:
    def __init__(self, name, number):
        self.image = pygame.image.load(rf".\karticky\{name}.png")
        self.number = number

    def draw_card(self, pos_x, pos_y):
        card = self.image.convert_alpha()
        card = pygame.transform.smoothscale(card, (200, 300)) # new image size
        gd.display.blit(card, (pos_x, pos_y))

seasons = [Card('18', 8), 
           Card('19', 8),
           Card('20', 7),
           Card('21', 6)]       

forrest_rules_cards = [Card('26', 0), 
                       Card('27', 0), 
                       Card('28', 0),
                       Card('29', 0)]

water_rules_cards = [Card('30', 0), 
                     Card('31', 0), 
                     Card('32', 0),
                     Card('33', 0)]

house_rules_cards = [Card('34', 0), 
                     Card('35', 0), 
                     Card('36', 0),
                     Card('37', 0)]

area_rules_cards = [Card('38', 0), 
                    Card('39', 0), 
                    Card('40', 0),
                    Card('41', 0)]

rules_cards = [random.choice(forrest_rules_cards), 
               random.choice(house_rules_cards), 
               random.choice(water_rules_cards),
               random.choice(area_rules_cards)]

monster_cards = [Card('01', 0), 
                 Card('02', 0), 
                 Card('03', 0),
                 Card('04', 0),
                 Card('A01', 0), 
                 Card('A02', 0), 
                 Card('A03', 0),
                 Card('A04', 0)]

complete_playing_cards = [Card('05', 0), 
                 Card('06', 0), 
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
                 Card('17', 0)]

extension_cards = [Card('S1', 0), 
                 Card('S2', 0), 
                 Card('S3', 0),
                 Card('S4', 0),
                 Card('S5', 0), 
                 Card('S6', 0), 
                 Card('S7', 0),
                 Card('S8', 0)]
    





