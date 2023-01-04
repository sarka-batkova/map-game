"""Definition of variables and methods used in other modules.

Attributes:
    white (tuple): RGB definition of white.
    black (tuple): RGB definition of black.
    red (tuple): RGB definition of red.
    dimension (float): Display dimension in pixels, used to determine the width and height of the game window.
    display_width (float): The width of the game window in pixels.
    display_height (float): The height of the game window in pixels.
    display (pygame.Surface): The display of the game window.

Methods:
    message(msg, color, font_size, pos_x, pos_y): Prints out a message on the screen.
    rect(color, pos_x, pos_y, size_x, size_y, border = 0): Draws a rectangle on the screen.
    line(color, start_x, start_y, end_x, end_y, width): Draws a line on the screen.
"""

import pygame

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

dimension = 700 
display_width = round(1.45 * dimension)    
display_height = round(dimension)

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Kartografove')

def message (msg, color, font_size, pos_x, pos_y):
    """Prints out a message on the screen.

    Args:
        msg (str): Message to print.
        color (str): Message color.
        font_size (float): Font size.
        pos_x (float): x position of the upper left corner in percents of the game window.
        pos_y (float): y position of the upper left corner in percents of the game window.    
    """
    font_style = pygame.font.SysFont(None, round((display_width/100)*font_size))
    message = font_style.render(msg, True, color)
    display.blit(message, [round((display_width/100)*pos_x), round((display_height/100)*pos_y)])

def rect (color, pos_x, pos_y, size_x, size_y, border = 0):
    """Draws a rectangle on the screen.
    
    Args:
        color (str): Rectangle color.
        pos_x (float): x position of the upeer left corner in percents of the game window.
        pos_y (float): y position of the upper left corner in percents of the game window.
        size_x (float): Rectangle width in percents of the game window.
        size_y (float): Rectangle height in percents of the game window.
        border (float): Rectangle border width in percents of the game window.
    """
    pygame.draw.rect(display, color, [round((display_width/100)*pos_x), round((display_height/100)*pos_y), round((display_height/100)*size_x), round((display_height/100)*size_y)], round((display_height/100)*border))

def line (color, start_x, start_y, end_x, end_y, width):
    """Draws a line on the screen.
    
    Args:
        color (str): Line color.
        start_x (float): x position of starting point in percents of the game window.
        start_y (float): y position of starting point in percents of the game window.
        end_x (float): x position of ending point in percents of the game window.
        end_y (float): y position of ending point in percents of the game window.
        width (float): Line width in percents of the game window.
    """
    pygame.draw.line(display, color, (round((display_width/100)*start_x), round((display_height/100)*start_y)), (round((display_width/100)*end_x), round((display_height/100)*end_y)), round((display_width/100)*width))
