# it imports pygame
import pygame
import random

pygame.init()

# setting the size of display/window
display_height = 500
display_width = 500

# creating the display/window. size in tuple
gameDisplay = pygame.display.set_mode((display_width,display_height))

clock = pygame.time.Clock()

# loading a image
images = pygame.image.load("linux.png")
object2 = pygame.image.load("/home/ryotakei/Downloads/pacman.png")
# setting the size. size in tuple
images = pygame.transform.scale(images, (60, 60))
object2 = pygame.transform.scale(object2, (60, 60))

linux_changeValue = 5
object_changeValue = 5


def random_movings(x, y):
    '''
    Get random x and y change values
    :param x: change x value of the object
    :param y: change y value of the object
    :return: new change x and y values
    '''
    number = random.randint(0, 100)
    if number == 4:
        return -object_changeValue, 0
    elif number == 7:
        return object_changeValue, 0
    elif number == 10:
        return 0, -object_changeValue
    elif number == 1:
        return 0, object_changeValue
    else:
        return x, y


def overX(x):
    '''
    It checks if x value is outside of the window
    :param x: x value of the object
    :return: new x value if the object is outside of the window
    '''
    if x < 0:
        return display_width
    elif x > display_width:
        return 0
    else:
        return x


def overY(y):
    '''
    It checks if y value is outside of the window
    :param y: y value of the object
    :return: new y value if the object is outside of the window
    '''
    if y < 0:
        return display_height
    elif y > display_height:
        return 0
    else:
        return y


def image(x, y, image):
    '''
    This function displays a image
    :param x: x pos of the image
    :param y: y pos of the image
    :param image: image you want to display
    :return: nothing
    '''
    gameDisplay.blit(image, (x, y))


# this is the main function
def main():
    # set the x and y pos of the image
    x = 200 # x = display_width / 2
    y = 20  # y = display_height / 2

    object_x = 100
    object_y = 100

    x_change = 0
    y_change = 0

    objectX_change = 0
    objectY_change = 0

    while True:
        # for every event that happens during the game.....
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # it exits out
                return

            # any keys pressed???
            if event.type == pygame.KEYDOWN:

                # is the key left arrow??
                if event.key == pygame.K_LEFT:
                    # changing the x value by -5 but not y
                    x_change = - linux_changeValue
                    y_change = 0

                # is the key right arrow??
                elif event.key == pygame.K_RIGHT:
                    # changing the x value by 5 but not y
                    x_change = linux_changeValue
                    y_change = 0

                # is the key up arrow??
                elif event.key == pygame.K_UP:
                    # changing the y value by 5 but not x
                    y_change = -linux_changeValue
                    x_change = 0

                # is the key down arrow??
                elif event.key == pygame.K_DOWN:
                    # changing the y value by 5 but not x
                    y_change = linux_changeValue
                    x_change = 0

            # if keys are up??
            if event.type == pygame.KEYUP:
                # if right arrow OR left arrow are not pressed
                if event.key == pygame.K_RIGHT | event.key == pygame.K_LEFT:
                    # Stopped changing the x and y
                    x_change = 0
                    y_change = 0
                # if up arrow OR down arrow are not pressed
                if event.key == pygame.K_UP | event.key == pygame.K_DOWN:
                    # Stopped changing the x and y
                    x_change = 0
                    y_change = 0

        # setting the background color. RGB in tuple
        gameDisplay.fill((100, 150, 255))

        temp_xchange = objectX_change
        temp_ychange = objectY_change

        objectX_change, objectY_change = random_movings(temp_xchange, temp_ychange)

        temp_x = x
        x = overX(temp_x)

        temp_y = y
        y = overY(temp_y)

        x += x_change # x = x + x_change
        y += y_change # y = y + y_change

        # calling the function
        # image(x, y, images)

        image(object_x, object_y, object2)

        # updates the display
        pygame.display.update()

        # setting FPS
        clock.tick(60)


if __name__ == '__main__':
    main()

# quits the game
pygame.quit()
