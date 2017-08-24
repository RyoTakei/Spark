import pygame

# creating the window
gameDisplay = pygame.display.set_mode((0, 0))


def image(x, y, image):
    '''
    this displays images on the display
    :param x: x pos of the image
    :param y: y pos of the image
    :param image: image that you want to show
    :return: nothing
    '''
    gameDisplay.blit(image, (x, y))
