import pygame
import random
import time

pygame.init()

display_height = 800
display_width = 800


gameDisplay = pygame.display.set_mode((display_width,display_height))

clock = pygame.time.Clock()


images = pygame.image.load("/home/ryotakei/Picture/linux.png")
images = pygame.transform.scale(images, (60, 60))

windows = pygame.image.load("/home/ryotakei/Picture/windows.png")
windows = pygame.transform.scale(windows, (60, 60))

apple = pygame.image.load("/home/ryotakei/Picture/apple.png")
apple = pygame.transform.scale(apple, (30, 30))

object_changeValue = 5
linux_changeValue = 5


def image(x, y, image):
    gameDisplay.blit(image, (x, y))


def collision(x1, y1, w1, h1, x2, y2, w2, h2):
    return x1 < x2 + w2 and y1 < y2 + h2 and x2 < x1 + w1 and y2 < y1 + h1


def text_object(text, font, color):
    textSurf = font.render(text, True, color)
    return textSurf, textSurf.get_rect()


def message_display(word, color):
    text = pygame.font.Font("/home/ryotakei/.fonts/Ubuntu.ttf", 50)
    textSufr, textRect = text_object(word, text, color)
    textRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(textSufr, textRect)

    pygame.display.update()

    time.sleep(3)


def clear():
    message_display("Good Job!", (0, 0, 255))
    pygame.quit()


def crashed():
    message_display("Crashed", (255, 0, 0))
    main()


def quit():
    pygame.draw.rect(gameDisplay, (255, 255, 255), [display_width - 100, display_height + 100, 80, 80])


def ramdom_movings(x, y):
    while True:
        number = random.randint(0, 100)
        if number == 3:
            return - object_changeValue, 0

        elif number == 7:
            return object_changeValue, 0

        elif number == 6:
            return 0, -object_changeValue

        elif number == 1:
            return 0, object_changeValue
        else:
            return x, y


def overX(x):
    if x < 0:
        return display_width

    if x > display_width:
        return 0

    return x


def overY(y):
    if y < 0:
        return display_height

    if y > display_height:
        return 0

    return y


def main():
    x = 200
    y = 200

    windows_ychange = 5
    windows_xchange = 5

    apple_xchange = 5
    apple_ychange = 5

    xPos = random.randrange(display_width / 2, display_width)
    yPos = random.randrange(display_height / 2, display_height)

    xApple = random.randrange(0, display_width)
    yApple = random.randrange(0, display_height)

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
                if event.key == pygame.K_UP | event.key == pygame.K_DOWN:
                    y_change = 0

        xVal = windows_xchange
        yVal = windows_ychange
        xVal2 = apple_xchange
        yVal2 = apple_ychange

        windows_xchange, windows_ychange = ramdom_movings(xVal, yVal)
        apple_xchange, apple_ychange = ramdom_movings(xVal2, yVal2)

        x = overX(x)
        y = overY(y)

        xPos = overX(xPos)
        yPos = overY(yPos)

        xApple = overX(xApple)
        yApple = overY(yApple)

        if collision(x, y, 60, 60, xPos, yPos, 60, 60):
            crashed()

        if collision(x, y, 60, 60, xApple, yApple, 30, 30):
            clear()

        gameDisplay.fill((100, 150, 255))

        x += x_change
        y += y_change

        xPos += windows_xchange
        yPos += windows_ychange

        xApple += apple_xchange
        yApple += apple_ychange

        image(x, y, images)
        image(xPos, yPos, windows)
        image(xApple, yApple, apple)

        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    level = 1
    main()

pygame.quit()