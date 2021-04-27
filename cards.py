import pygame
import random

import global_def as gd


def message(msg, color, font_size, x, y):
    gd.display.blit(pygame.font.SysFont(None, font_size).render(msg, True, color), [x, y])

def draw_letter(letter, pos_x, pos_y):
    pygame.draw.rect(gd.display, gd.black, [pos_x, pos_y, 200, 150], 10)
    message(letter, gd.red, 100, pos_x + 75, pos_y + 55)

class Card:
    def __init__(self, image, number):
        self.image = image
        self.number = number

    def draw_card(self, pos_x, pos_y):
        card = self.image.convert_alpha()
        card = pygame.transform.smoothscale(card, (200, 300)) # new image size
        gd.display.blit(card, (pos_x, pos_y))

Seasons = [Card(pygame.image.load(r'C:\Users\batkova\Downloads\karticky\karticky\18.png'), 8), 
            Card(pygame.image.load(r'C:\Users\batkova\Downloads\karticky\karticky\19.png'), 8),
            Card(pygame.image.load(r'C:\Users\batkova\Downloads\karticky\karticky\20.png'), 7),
            Card(pygame.image.load(r'C:\Users\batkova\Downloads\karticky\karticky\21.png'), 6)]       


Forrest_rules_cards = [Card(pygame.image.load(r'C:\Users\batkova\Downloads\karticky\karticky\26.png'), 0), 
                        Card(pygame.image.load(r'C:\Users\batkova\Downloads\karticky\karticky\27.png'), 0), 
                        Card(pygame.image.load(r'C:\Users\batkova\Downloads\karticky\karticky\28.png'), 0),
                        Card(pygame.image.load(r'C:\Users\batkova\Downloads\karticky\karticky\29.png'), 0)]

Water_rules_cards = [Card(pygame.image.load(r'C:\Users\batkova\Downloads\karticky\karticky\30.png'), 0), 
                        Card(pygame.image.load(r'C:\Users\batkova\Downloads\karticky\karticky\31.png'), 0), 
                        Card(pygame.image.load(r'C:\Users\batkova\Downloads\karticky\karticky\32.png'), 0),
                        Card(pygame.image.load(r'C:\Users\batkova\Downloads\karticky\karticky\33.png'), 0)]

House_rules_cards = [Card(pygame.image.load(r'C:\Users\batkova\Downloads\karticky\karticky\34.png'), 0), 
                        Card(pygame.image.load(r'C:\Users\batkova\Downloads\karticky\karticky\35.png'), 0), 
                        Card(pygame.image.load(r'C:\Users\batkova\Downloads\karticky\karticky\36.png'), 0),
                        Card(pygame.image.load(r'C:\Users\batkova\Downloads\karticky\karticky\37.png'), 0)]

Area_rules_cards = [Card(pygame.image.load(r'C:\Users\batkova\Downloads\karticky\karticky\38.png'), 0), 
                        Card(pygame.image.load(r'C:\Users\batkova\Downloads\karticky\karticky\39.png'), 0), 
                        Card(pygame.image.load(r'C:\Users\batkova\Downloads\karticky\karticky\40.png'), 0),
                        Card(pygame.image.load(r'C:\Users\batkova\Downloads\karticky\karticky\41.png'), 0)]

Rules_cards = [random.choice(Forrest_rules_cards), 
            random.choice(House_rules_cards), 
            random.choice(Water_rules_cards),
            random.choice(Area_rules_cards)]

Monster_cards = [Card(pygame.image.load(r'C:\Users\batkova\Downloads\karticky\karticky\01.png'), 0), 
                Card(pygame.image.load(r'C:\Users\batkova\Downloads\karticky\karticky\02.png'), 0), 
                Card(pygame.image.load(r'C:\Users\batkova\Downloads\karticky\karticky\03.png'), 0),
                Card(pygame.image.load(r'C:\Users\batkova\Downloads\karticky\karticky\04.png'), 0),
                Card(pygame.image.load(r'C:\Users\batkova\Downloads\karticky\karticky\A01.png'), 0), 
                Card(pygame.image.load(r'C:\Users\batkova\Downloads\karticky\karticky\A02.png'), 0), 
                Card(pygame.image.load(r'C:\Users\batkova\Downloads\karticky\karticky\A03.png'), 0),
                Card(pygame.image.load(r'C:\Users\batkova\Downloads\karticky\karticky\A04.png'), 0)]

Playing_cards = [Card(pygame.image.load(r'C:\Users\batkova\Downloads\karticky\karticky\05.png'), 0), 
                Card(pygame.image.load(r'C:\Users\batkova\Downloads\karticky\karticky\06.png'), 0), 
                Card(pygame.image.load(r'C:\Users\batkova\Downloads\karticky\karticky\07.png'), 1),
                Card(pygame.image.load(r'C:\Users\batkova\Downloads\karticky\karticky\08.png'), 1),
                Card(pygame.image.load(r'C:\Users\batkova\Downloads\karticky\karticky\09.png'), 1), 
                Card(pygame.image.load(r'C:\Users\batkova\Downloads\karticky\karticky\10.png'), 1), 
                Card(pygame.image.load(r'C:\Users\batkova\Downloads\karticky\karticky\11.png'), 2),
                Card(pygame.image.load(r'C:\Users\batkova\Downloads\karticky\karticky\12.png'), 2),
                Card(pygame.image.load(r'C:\Users\batkova\Downloads\karticky\karticky\13.png'), 2),
                Card(pygame.image.load(r'C:\Users\batkova\Downloads\karticky\karticky\14.png'), 2), 
                Card(pygame.image.load(r'C:\Users\batkova\Downloads\karticky\karticky\15.png'), 2), 
                Card(pygame.image.load(r'C:\Users\batkova\Downloads\karticky\karticky\16.png'), 2),
                Card(pygame.image.load(r'C:\Users\batkova\Downloads\karticky\karticky\17.png'), 0)]
    





