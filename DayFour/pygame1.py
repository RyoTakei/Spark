import pygame

pygame.init()

display_height = 800
display_width = 800

gameDisplay = pygame.display.set_mode((display_height, display_width))

clock = pygame.time.Clock()

crashed = False

images = pygame.image.load("/home/ryotakei/Picture/linux.png")
images = pygame.transform.scale(images, (60, 60))
def image(x, y):
    gameDisplay.blit(images, (x, y))

x = display_width * 0.5
y = display_height * 0.5

x_change = 0
y_change = 0

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
                y_change = 0
            elif event.key == pygame.K_RIGHT:
                x_change = 5
                y_change = 0
            elif event.key == pygame.K_UP:
                y_change = -5
                x_change = 0
            elif event.key == pygame.K_DOWN:
                y_change = 5
                x_change = 0

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT | event.key == pygame.K_LEFT:
                x_change = 0
            if event.key == pygame.K_UP | event.key == pygame.K_DOWN:
                y_change = 0

    gameDisplay.fill((255, 255, 255))

    x += x_change
    y += y_change

    image(x, y)
    pygame.display.update()
    clock.tick(60)

pygame.quit()