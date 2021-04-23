import pygame
import random

import global_def as gd


def message(msg, color, font_size, x, y):
    gd.display.blit(pygame.font.SysFont(None, font_size).render(msg, True, color), [x, y])

class TextCard:
    def __init__(self, text, color, font_size, pos_x, pos_y):
        self.text = text
        self.color = color
        self.font_size = font_size
        self.pos_x = pos_x
        self.pos_y = pos_y 

    def draw_text_card(self):
        pygame.draw.rect(gd.display, gd.black, (self.pos_x, self.pos_y, 150, 200), 10)
        message(self.text, self.color, self.font_size, self.pos_x+40, self.pos_y+60)

Jaro = TextCard("Jaro: A+B", gd.black, 50, 200, 160)
A = TextCard("A", gd.red, 120, 200, 400)
B = TextCard("B", gd.red, 120, 400, 400)
C = TextCard("C", gd.red, 120, 600, 400)
D = TextCard("D", gd.red, 120, 800, 400)

Forrest_rules_cards = [TextCard("Spoj hory", gd.red, 50, 200, 700), 
                        TextCard("okraj", gd.red, 50, 200, 700), 
                        TextCard("obkruz", gd.red, 50, 200, 700)]

House_rules_cards = [TextCard("Vetsi nez 8", gd.red, 50, 400, 700), 
                        TextCard("Nedotykat hory", gd.red, 50, 400, 700), 
                        TextCard("Druhe nejvetsi", gd.red, 50, 400, 700)]

Water_rules_cards = [TextCard("Dotek s polem", gd.red, 50, 400, 700), 
                        TextCard("Dotek s horou", gd.red, 50, 400, 700), 
                        TextCard("Nedotek s polem", gd.red, 50, 400, 700)]

Area_rules_cards = [TextCard("Nejvetsi ctverec", gd.red, 50, 400, 700), 
                        TextCard("Radek nebo sloupec", gd.red, 50, 400, 700), 
                        TextCard("Diagonala", gd.red, 50, 400, 700)]

Rules_cards = [random.choice(Forrest_rules_cards), 
            random.choice(House_rules_cards), 
            random.choice(Water_rules_cards),
            random.choice(Area_rules_cards)]
    

class PlayingCard:
  def __init__(self, text, shape, terrain, number):
    # super().__init__(text)
    self.text = text
    self.shape = shape
    self.terrain = terrain
    self.number = number

# class RulesCard:



