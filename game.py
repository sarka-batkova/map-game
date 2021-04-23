import pygame
import random

import global_def as gd
import cards as c


pygame.init()

gd.display.fill(gd.white)
c.A.draw_text_card()
c.B.draw_text_card()
c.C.draw_text_card()
c.D.draw_text_card()
c.Jaro.draw_text_card()

c.random.choice(c.Rules_cards).draw_text_card()


c.message("Press n for next card", gd.black, 40, 20, 50)

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
