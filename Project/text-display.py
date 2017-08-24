import pygame
import time

# setting the width and height of the display
display_width = 0
display_height = 0

# creating the window
gameDisplay = pygame.display.set_mode((display_width,display_height))


def text_object(text, font, color):
    '''
    :param text: text you want to display
    :param font: font you want to use
    :param color: color you want your text to be. RGB in tuple
    :return: text surface, and text rectangle
    '''
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def message_display(word, color):
    '''
    This displays text on the center of the display
    :param word: word you want to display
    :param color: color. RGB in tuple
    :return: nothing
    '''

    text = pygame.font.Font("/path/to/the/font", 50)
    # calling the text_object function
    textSufrace, textRect = text_object(word, text, color)
    textRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(textSufrace, textRect)

    # updating the display after displaying the text
    pygame.display.update()

    # optional!!!!
    # it waits for 3 second
    time.sleep(3)