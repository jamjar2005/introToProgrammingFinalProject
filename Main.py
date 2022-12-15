'''
goals: 
- Using Pygame to create launch/thrust animations and a smoke trail along with moving debris.
- Reach the finish line
rules:
- Must reach finish line
Feedback:
- You win if you reach the finish line
Freedom:
- You can press G to ignite rocket and move laterally

'''
# James Haven - Period 3

# sources:
# Mr. Cozort's source code files
# for help with particles: https://www.youtube.com/watch?v=yfcsB3SGsKY (Clear code)
# for help with sprites: https://www.youtube.com/watch?v=hDu8mcAlY4E (Clear code)

# import libraries
import pygame as pg
from pygame.sprite import Sprite
import os
from random import *

# importing reated modules or libraries
from settings import *

# importing global variables
vec = pg.math.Vector2

# setting up asset folders (Used for sprite images later)
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')

# defining a function for drawing on-screen text
def draw_text(text, size, color, x, y):
    font_name = pg.font.match_font('calibri')
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    screen.blit(text_surface, text_rect)

# Creating the class "Player" for my rocket sprite
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
    # defining the function "controls" to create controls for class "Player"
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
        # using a conditional statement to create a launching animation
        if keys[pg.K_g]:
            player.rect.y -= 1.01
            ground.rect.y += 1
            moon.rect.y += 1
            # setting spawn location for exhaust function using self.pos + integers
            exhaust(self.pos[0] + 195 , self.pos[1] + 375)
    # updating class Player (self) and calling self.controls() function
    def update(self):
        self.acc = vec(0,0)
        self.controls()
        # adding friction
        self.acc.x += self.vel.x * -0.1
        # adding movement and position rules
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect = self.pos

# creating class "Ground" for the ground
class Ground(Sprite):
    def __init__(self, x, y, w, h):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(DARK_GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# creating class "Moon" for the moon
class Moon(Sprite):
    def __init__(self):
        Sprite. __init__(self)
        # importing an image for Player sprite from asset folder "images"
        self.image = pg.image.load(os.path.join(img_folder, 'My project (9).png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/1.2, HEIGHT/4)
        self.pos = vec(WIDTH, HEIGHT)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        print(self.rect.center)

# creating class "Debris" for space debris
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
        self.rect.y += 5

# crating class "Smoke" for rocket trail
class Smoke(Sprite):
    def __init__(self, x, y, w, h, color):
        Sprite. __init__(self)
        self.image = pg.Surface((w, h))
        self.color = color
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    # defining update(self) function and randint to create possibl spawn area for class "Smoke" (rocket trail)
    def update(self):
        self.rect.x += 5 * choice([-1,1])
        self.rect.y += 5 * randint(1,3)
        # using a conditional statement to kill sprites via self.kill() method if sprites are lower than screen
        if self.rect.y > HEIGHT:
            self.kill()

# creating class "Barrier" for invisible barrier
class Barrier(Sprite):
    def __init__(self, x, y, w, h):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
# initializing pygame and creating a visible window
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Space Voyager")
clock = pg.time.Clock()

# creating groups for classes
all_sprites = pg.sprite.Group()
all_plats = pg.sprite.Group()
debris = pg.sprite.Group()
smokes = pg.sprite.Group()

# instantiating classes
player = Player()
ground = Ground(0, HEIGHT/1.05, WIDTH, 50)
moon = Moon()
barrier = Barrier(0, HEIGHT/300, WIDTH, 1)

# defining function "exhaust()" and parameters "x, y" and using "i in range" to spawn in anywhere from 1-3 sprites per refresh
# also defining x, y, dimensions, and color
def exhaust(x,y):
    for i in range (3):
        e = Smoke(x, y, 25, 25, RED)
        # adding class "Smoke" to groups "smokes" and "all_sprites"
        smokes.add(e)
        all_sprites.add(e)

# defining function "Spawn()" and parameter "n" 
# using randint to spawn sprites from class "Debris" randomly anywhere within the given dimensions.
def spawn(n):
    for i in range(n):
        m = Debris(randint(0, WIDTH), randint(0, HEIGHT/2), 25, 25, (ORANGE))
        # adding "m" to groups "all_sprites" and "debris" and printing "m" for reference/tests
        all_sprites.add(m)
        debris.add(m)
        print(m)
# calling function "spawn()" ten times
spawn(10)

# adding instances to groups
all_sprites.add(player, moon)
all_plats.add(ground, barrier)

# game loop (while loop)
running = True
while running:
    #this keeps the game running using the clock
    clock.tick(FPS)

    # checking where mobs are and killing them if they are off screen using "m.kill()" method
    for m in debris:
        if m.rect.y > HEIGHT:
            m.kill()
            print(len(debris))
    # this checks if there are below 7 mobs on screen and spawns more
    if len(debris) < 7:
        spawn(15)

    # using a for loop to check for closed window
    for event in pg.event.get():
        # checking for closed window
        if event.type == pg.QUIT:
            running = False

    # updating groups
    all_sprites.update()
    all_plats.update()

    # using a for loop to check if sprites in the debris group pass by the bottom of the screen and print a message if so
    for d in debris:
        if d.rect.y > HEIGHT:
            print("passed.y...")
    
# drawing the background screen
    screen.fill(BLACK)
    all_sprites.draw(screen)
    all_plats.draw(screen)

    # drawing global variable ALTITUDE on the screen.
    draw_text("Altitude: " + str(ALTITUDE), 22, BLUE, WIDTH/12, HEIGHT/1.15)

    # using conditional statements to display an altitude number on the screen if the rocket passes a certain height
    # each number corresponds to a certain sector of the screen
    if player.rect.y <= (HEIGHT/3):
        draw_text("Altitude: " + str(ALTITUDE + 10000), 22, CYAN, WIDTH/12, HEIGHT/1.5)
    if player.rect.y <= (HEIGHT/5):
        draw_text("Altitude: " + str(ALTITUDE + 20000), 22, GREEN, WIDTH/12, HEIGHT/2)
    if player.rect.y <= (HEIGHT/10):
        draw_text("Altitude: " + str(ALTITUDE + 30000), 22, ORANGE, WIDTH/12, HEIGHT/3)
    if player.rect.y <= (HEIGHT/200):
        draw_text("Altitude: " + str(ALTITUDE + 40000), 22, RED, WIDTH/12, HEIGHT/4.5)
        

    # using a conditional statment to display "YOU WIN" on screen if player.rect.y is <= barrier.rect.y
    if player.rect.y <= (barrier.rect.y):
        draw_text("YOU WIN " + str(WINNER), + 125, GREEN, WIDTH/2, HEIGHT/5)

    # buffer, flips display after everything is drawn
    pg.display.flip()
pg.quit()
