'''
Using Pygame to create launch/thrust animations and a smoke trail, 
along with a changing background based on altitude and an altimeter.

'''

# sources:
# Mr. Cozort's source code files
# for help with particles: https://www.youtube.com/watch?v=yfcsB3SGsKY (Clear code)
# for help with background images: https://www.youtube.com/watch?v=WurCpmHtQc4 (Codemy.com)
# for help with sprites: https://www.youtube.com/watch?v=hDu8mcAlY4E (Clear code)
# for help with jpeg sprites: https://www.youtube.com/watch?v=M6e3_8LHc7A (Coding With Russ)

# import libraries
import pygame as pg
from pygame.sprite import Sprite
import os

# built in

# installed modules or libraries

# created modules or libraries
from settings import *

# global variables
vec = pg.math.Vector2
# utilit

# setting up asset folders (Used for sprite later)
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')


# Creating a class for my rocket sprite
class Player(Sprite):
    def __init__(self):
        Sprite. __init__(self)
        # using an image for Player sprite
        self.image = pg.image.load(os.path.join(img_folder, 'pixil-frame-0 (1).png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/1.3)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        print(self.rect.center)
    def controls(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.acc.x = -5
        if keys[pg.K_d]:
            self.acc.x = 5
    def update(self):
        self.acc = vec(0,0)
        self.controls()
        # adding friction
        self.acc.x += self.vel.x * -0.1
        # add y
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect = self.pos

# initializing pygame and creating a visible window
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Space Voyager")
clock = pg.time.Clock()

# creating a group for all of my sprites
all_sprites = pg.sprite.Group()

# instantiating classes
player = Player()

# adding these instances to groups
all_sprites.add(player)

# game loop (while loop)
running = True 
while running:
    #this keeps the game running using the clock
    clock.tick(FPS)

    for event in pg.event.get():
        # checking for closed window
        if event.type == pg.QUIT:
            running = False
    
    # update
    # updating all sprites
    all_sprites.update()
                
# drawing the background screen
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # buffer, flips display after everything is drawn
    pg.display.flip()
pg.quit()
