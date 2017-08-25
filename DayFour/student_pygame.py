# it imports pygame
import pygame

pygame.init()

# setting the size of display/window
display_height = 500
display_width = 500

# creating the display/window. size in tuple
gameDisplay = pygame.display.set_mode((display_width,display_height))

clock = pygame.time.Clock()

# loading a image
images = pygame.image.load("linux.png")
# setting the size. size in tuple
images = pygame.transform.scale(images, (60, 60))

linux_changeValue = 5


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

    x_change = 0
    y_change = 0

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
                elif event.key == pygame.K_DOWN:
                    y_change = linux_changeValue
                    x_change = 0

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT | event.key == pygame.K_LEFT:
                    x_change = 0
                    y_change = 0
                if event.key == pygame.K_UP | event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = 0



        gameDisplay.fill((100, 150, 255))

        x += x_change
        y += y_change


        image(x, y, images)
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()

pygame.quit()