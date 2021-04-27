import pygame
import random

import global_def as gd


def message(msg, color, font_size, x, y):
    gd.display.blit(pygame.font.SysFont(None, font_size).render(msg, True, color), [x, y])

class Card:
    def __init__(self, image, number):
        self.image = image
        self.number = number

    def draw_card(self, pos_x, pos_y):
        card = self.image.convert_alpha()
        card = pygame.transform.smoothscale(card, (200, 300)) # new image size
        gd.display.blit(card, (pos_x, pos_y))
        


Forrest_rules_cards = [Card(pygame.image.load(r'C:\Users\batkova\Downloads\karticky\karticky\26.png'), 0), 
                        Card(pygame.image.load(r'C:\Users\batkova\Downloads\karticky\karticky\27.png'), 0), 
                        Card(pygame.image.load(r'C:\Users\batkova\Downloads\karticky\karticky\28.png'), 0),
                        Card(pygame.image.load(r'C:\Users\batkova\Downloads\karticky\karticky\29.png'), 0)]

House_rules_cards = [Card(pygame.image.load(r'C:\Users\batkova\Downloads\karticky\karticky\34.png'), 0), 
                        Card(pygame.image.load(r'C:\Users\batkova\Downloads\karticky\karticky\35.png'), 0), 
                        Card(pygame.image.load(r'C:\Users\batkova\Downloads\karticky\karticky\36.png'), 0),
                        Card(pygame.image.load(r'C:\Users\batkova\Downloads\karticky\karticky\37.png'), 0)]

Water_rules_cards = [Card(pygame.image.load(r'C:\Users\batkova\Downloads\karticky\karticky\30.png'), 0), 
                        Card(pygame.image.load(r'C:\Users\batkova\Downloads\karticky\karticky\31.png'), 0), 
                        Card(pygame.image.load(r'C:\Users\batkova\Downloads\karticky\karticky\32.png'), 0),
                        Card(pygame.image.load(r'C:\Users\batkova\Downloads\karticky\karticky\33.png'), 0)]

Area_rules_cards = [Card(pygame.image.load(r'C:\Users\batkova\Downloads\karticky\karticky\38.png'), 0), 
                        Card(pygame.image.load(r'C:\Users\batkova\Downloads\karticky\karticky\39.png'), 0), 
                        Card(pygame.image.load(r'C:\Users\batkova\Downloads\karticky\karticky\40.png'), 0),
                        Card(pygame.image.load(r'C:\Users\batkova\Downloads\karticky\karticky\41.png'), 0)]

Rules_cards = [random.choice(Forrest_rules_cards), 
            random.choice(House_rules_cards), 
            random.choice(Water_rules_cards),
            random.choice(Area_rules_cards)]
    





