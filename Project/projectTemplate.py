import pygame

pygame.init()

# setting the height and width of the window
display_height = 800
display_width = 800

# creating the window.
gameDisplay = pygame.display.set_mode((display_width, display_height))

# setting the clock
clock = pygame.time.Clock()


def main():
    '''
    main function.
    it will return when the game is over.
    '''
    while True:
        for event in pygame.event.get():
            # if event type is quit, it'll end the game
            if event.type == pygame.QUIT:
                return

            # when any key is pressed
            if event.type == pygame.KEYDOWN:

                # and the left arrow is pressed
                if event.key == pygame.K_LEFT:
                    '''
                    something you want the program to do when
                    theleft arrow is pressed
                    '''
                    pass

                # or the right arrow is pressed
                elif event.key == pygame.K_RIGHT:
                    '''
                    something you want the program to do when
                    the right arrow is pressed
                    '''
                    pass

                # or the up arrow is pressed
                elif event.key == pygame.K_UP:
                    '''
                    something you want your program to do when
                    the up arrow is pressed
                    '''
                    pass

                # or the down arrow is pressed
                elif event.key == pygame.K_DOWN:
                    '''
                    something you want your program to do when
                    the down arrow is pressed
                    '''
                    pass

            # if any key is not pressed
            if event.type == pygame.KEYUP:

                # and if the right arrow is not pressed
                if event.key == pygame.K_RIGHT:
                    '''
                    something you want your program to do when 
                    the user is not pressing the right arrow key
                    '''
                    pass

                # and if the left arrow is not pressed
                if event.key == pygame.K_LEFT:
                    '''
                    something you want your program to do when 
                    the user is not pressing the left arrow key
                    '''
                    pass

                # and if the up key is not pressed
                if event.key == pygame.K_UP:
                    '''
                    something you want your program to do when 
                    the user is not pressing the up arrow key
                    '''
                    pass

                # and if the down arrow is not pressed
                if event.key == pygame.K_DOWN:
                    '''
                    something you want your program to do when
                    the user is not pressing the down arrow key
                    '''

        # setting the background color. RGB value in tuple
        gameDisplay.fill((0, 0, 0))

        # updating the display.
        # Call this function whenever you create a new object
        pygame.display.update()

        # sets FPS. How many times it updates the display per second.
        clock.tick(60)


# this will call main() if this file is directly executed.
if __name__ == '__main__':
    main()

# when everything is done. pygame will quite the game
pygame.quit()