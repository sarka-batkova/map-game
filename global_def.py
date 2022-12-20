import pygame
import random

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

dimension = 700

display_width = round(1.45 * dimension)    
display_height = round(dimension)

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Kartografove')

def message (msg, color, font_size, pos_x, pos_y):
    font_style = pygame.font.SysFont(None, round((display_width/100)*font_size))
    message = font_style.render(msg, True, color)
    display.blit(message, [round((display_width/100)*pos_x), round((display_height/100)*pos_y)])

def rect (color, pos_x, pos_y, size_x, size_y, border = 0):
    pygame.draw.rect(display, color, [round((display_width/100)*pos_x), round((display_height/100)*pos_y), round((display_height/100)*size_x), round((display_height/100)*size_y)], round((display_height/100)*border))

def line (color, start_x, start_y, end_x, end_y, width):
    pygame.draw.line(display, color, (round((display_width/100)*start_x), round((display_height/100)*start_y)), (round((display_width/100)*end_x), round((display_height/100)*end_y)), round((display_width/100)*width))

