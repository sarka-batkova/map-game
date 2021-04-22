import pygame
import random
import cards

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

 



def draw_text_card (pos_x, pos_y, msg, color, font_size):
    pygame.draw.rect(display, black, (pos_x, pos_y, 150, 200), 10)
    message(msg, color, font_size, pos_x+40, pos_y+60)

# def draw_play_card

display.fill(white)
draw_text_card(200,400,"A",red,120)
draw_text_card(400,400,"B",red,120)
draw_text_card(600,400,"C",red,120)
draw_text_card(800,400,"D",red,120)

draw_text_card(200,160,"Jaro: A+B",red,50)

# cards.Jaro.draw_card(display)

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
