import sys, pygame
import random
import time
from pygame.locals import *

surface = pygame.display.set_mode((800, 600))
pygame.display.set_caption("snake")

white = 255, 255, 255
black = 0, 0, 0
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255

speed = 15

left = False
right = False
up = False
down = False


class snake:
    x = 60
    y = 60


class food:
    x = random.randrange(0, 800, 15)
    y = random.randrange(0, 600, 15)


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and right == False:
                left = True
                right = False
                up = False
                down = False
            if event.key == pygame.K_RIGHT and left == False:
                left = False
                right = True
                up = False
                down = False
            if event.key == pygame.K_UP and down == False:
                left = False
                right = False
                up = True
                down = False
            if event.key == pygame.K_DOWN and up == False:
                left = False
                right = False
                up = False
                down = True
        # elif event.type == pygame.KEYUP:
        #     if event.key == pygame.K_LEFT:
        #         left = False
        #     if event.key == pygame.K_RIGHT:
        #         right = False
        #     if event.key == pygame.K_UP:
        #         up = False
        #     if event.key == pygame.K_DOWN:
        #         down = False

    time.sleep(100.0 / 2000.0);

    if left:
        snake.x -= speed
        if snake.x == -15:
            snake.x += 815
    if right:
        snake.x += speed
        if snake.x == 800:
            snake.x -= 800
    if up:
        snake.y -= speed
        if snake.y == -15:
            snake.y += 600
    if down:
        snake.y += speed
        if snake.y == 600:
            snake.y -= 600

    surface.fill(black)
    pygame.draw.rect(surface, white, (snake.x, snake.y, 15, 15))
    pygame.draw.rect(surface, red, (food.x, food.y, 15, 15))
    pygame.display.update()
