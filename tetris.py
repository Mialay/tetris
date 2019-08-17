import pygame, sys
import time

black = 0, 0, 0
white = 255, 255, 255

class long_cube:
    x = 200 - (150/2)
    y = 0

speed = 50

down = True

surface = pygame.display.set_mode((400, 600))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if down:
        long_cube.y -= speed

    time.sleep(100.0 / 200.0)

    surface.fill(black)
    pygame.draw.rect(surface, white, (long_cube.x, long_cube.y, 150, 25))
    pygame.display.update()