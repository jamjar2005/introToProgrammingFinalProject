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
from random import *

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

# defining a function for an altimeter 
def draw_text(text, size, color, x, y):
    font_name = pg.font.match_font('calibri')
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    screen.blit(text_surface, text_rect)

# Creating a class for my rocket sprite
class Player(Sprite):
    def __init__(self):
        Sprite. __init__(self)
        # using an image for Player sprite
        self.image = pg.image.load(os.path.join(img_folder, 'pixil-frame-0 (1).png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/3, HEIGHT/2.2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        print(self.rect.center)
    def controls(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.acc.x = -5
        if keys[pg.K_d]:
            self.acc.x = 5
        if keys[pg.K_LEFT]:
            self.acc.x = -5
        if keys[pg.K_RIGHT]:
            self.acc.x = 5
        if keys[pg.K_g]:
            player.rect.y -= 1.5
            ground.rect.y += 1
            moon.rect.y += 1
        '''else: 
            player.rect.y += 1.5
            ground.rect.y -= 1
            moon.rect.y -= 1'''
    def update(self):
        self.acc = vec(0,0)
        self.controls()
        # adding friction
        self.acc.x += self.vel.x * -0.1
        # add y
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect = self.pos

# creating a class for the ground
class Ground(Sprite):
    def __init__(self, x, y, w, h):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(DARK_GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# creating a class for the moon
class Moon(Sprite):
    def __init__(self):
        Sprite. __init__(self)
        # using an image for Player sprite
        self.image = pg.image.load(os.path.join(img_folder, 'My project (9).png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/1.2, HEIGHT/4)
        self.pos = vec(WIDTH, HEIGHT)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        print(self.rect.center)

# creating a class for asteroids/space debris
class Debris(Sprite):
    def __init__(self, x, y, w, h, color):
        Sprite. __init__(self)
        self.image = pg.Surface((w, h))
        self.color = color
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update(self):
        self.rect.y += 1

# creating a class for an invisible barrier
class Barrier(Sprite):
    def __init__(self, x, y, w, h):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
# initializing pygame and creating a visible window
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Space Voyager")
clock = pg.time.Clock()

# creating groups
all_sprites = pg.sprite.Group()
all_plats = pg.sprite.Group()
debris = pg.sprite.Group()

# instantiating classes
player = Player()
ground = Ground(0, HEIGHT/1.05, WIDTH, 50)
moon = Moon()
barrier = Barrier(0, HEIGHT/4, WIDTH, 1)
for i in range(100):
    m = Debris(randint(0, WIDTH), randint(0, HEIGHT), 25, 25, (ORANGE))
    all_sprites.add(m)
    debris.add(m)
    print(m)
# adding instances to groups
all_sprites.add(player, moon)
all_plats.add(ground, barrier)
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
    all_plats.update()
                
# drawing the background screen
    screen.fill(BLACK)
    all_sprites.draw(screen)
    all_plats.draw(screen)
    draw_text("Altitude: " + str(ALTITUDE), 22, BLUE, WIDTH/12, HEIGHT/1.15)
    draw_text("Strength: " + str(STRENGTH), 22, RED, WIDTH/1.12, HEIGHT/1.15)
    # buffer, flips display after everything is drawn
    pg.display.flip()
pg.quit()
