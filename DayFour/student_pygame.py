import pygame

pygame.init()

display_height = 800
display_width = 800


gameDisplay = pygame.display.set_mode((display_width,display_height))

clock = pygame.time.Clock()


images = pygame.image.load("linux.png")
images = pygame.transform.scale(images, (60, 60))

# object_changeValue = 5
linux_changeValue = 5


def image(x, y, image):
    gameDisplay.blit(image, (x, y))


def main():
    x = 200
    y = 20

    x_change = 0
    y_change = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -linux_changeValue
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = linux_changeValue
                    y_change = 0
                elif event.key == pygame.K_UP:
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