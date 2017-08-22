import pygame
import random
import time

pygame.init()

display_height = 800
display_width = 800

gameDisplay = pygame.display.set_mode((display_width, display_height))

clock = pygame.time.Clock()

linux = pygame.image.load("/home/ryotakei/Picture/linux.png")
linux = pygame.transform.scale(linux, (50, 50))


def display_image(image, x, y):
    gameDisplay.blit(image, (x, y))


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        x = random.randint(0, display_width)
        y = random.randint(0, display_height)

        display_image(linux, x, y)
        time.sleep(1)

        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    main()

pygame.quit()

