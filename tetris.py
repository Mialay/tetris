import pygame, sys
import time
import random

black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
speed = 25
surface = pygame.display.set_mode((400, 600))
cube_list = []
cube_group = pygame.sprite.Group()

size = []
long = (100, 25)
cube = (50, 50)
size.append(long)
size.append(cube)


def create_new(pos):
    _ = Cube(pos)
    cube_list.append(_)
    print(cube_list)


class Cube():
    def __init__(self, pos):
        self.width = pos[0]
        self.height = pos[1]
        self.pos_x = 200 - (self.width / 2)
        self.pos_y = 0 - self.height
        self.pos = (self.pos_x, self.pos_y)
        self.down = True

    def collision_with(self):
        return pygame.sprite.spritecollideany(self, cube_group)

    def draw(self):
        pygame.draw.rect(surface, white, (self.pos_x, self.pos_y, self.width, self.height))

    def turn(self):
        placeholder = self.height
        self.height = self.width
        self.width = placeholder


first_cube = Cube(long)
cube_list.append(first_cube)
print(cube_list)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and cube_list[-1].pos_x > 0:
                cube_list[-1].pos_x -= speed
            if event.key == pygame.K_RIGHT and cube_list[-1].pos_x < 400 - cube_list[-1].width:
                cube_list[-1].pos_x += speed
            if event.key == pygame.K_SPACE:
                if cube_list[-1].pos_y < 600 - cube_list[-1].width:
                    cube_list[-1].turn()

    for i in cube_list:
        if i.pos_y == 600 - i.height and i.down:
            i.down = False
            cube_group.add(i)
            create_new(random.choice(size))

    for i in cube_list:
        if i.down:
            i.pos_y += speed

    time.sleep(100.0 / 800.0)

    surface.fill(black)
    for i in cube_list:
        i.draw()
    pygame.display.update()
