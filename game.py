import pygame
import random


pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
display_width = 1500    
display_height = 1000

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Kartografove')


def message(msg, color, font_size, x, y):
    display.blit(pygame.font.SysFont(None, font_size).render(msg, True, color), [x, y])

class TextCard:
    def __init__(self, text, color, font_size, pos_x, pos_y):
        self.text = text
        self.color = color
        self.font_size = font_size
        self.pos_x = pos_x
        self.pos_y = pos_y 

    def draw_text_card(self):
        pygame.draw.rect(display, black, (self.pos_x, self.pos_y, 150, 200), 10)
        message(self.text, self.color, self.font_size, self.pos_x+40, self.pos_y+60)

Jaro = TextCard("Jaro: A+B", black,50,200,160)
A = TextCard("A", red,120,200,400)
B = TextCard("B", red,120,400,400)
C = TextCard("C", red,120,600,400)
D = TextCard("D", red,120,800,400)

display.fill(white)
A.draw_text_card()
B.draw_text_card()
C.draw_text_card()
D.draw_text_card()
Jaro.draw_text_card()

message("Press n for next card", black, 40, 20, 50)

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





# image = pygame.image.load(r'C:\Users\user\Pictures\geek.jpg')
# display_surface.blit(image, (0, 0))
