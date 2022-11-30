'''
Using Pygame to create launch/thrust animations and a smoke trail, 
along with a changing background based on altitude and an altimeter.

'''

# sources:
# Mr. Cozort's source code files
# for help with particles: https://www.youtube.com/watch?v=yfcsB3SGsKY (Clear code)
# for help with background images: https://www.youtube.com/watch?v=WurCpmHtQc4 (Codemy.com)
# for help with sprites: https://www.youtube.com/watch?v=hDu8mcAlY4E (Clear code)

# import libraries
import pygame as pg

# built in

# installed modules or libraries

# created modules or libraries
from settings import *

# global variables

# utilit

# initializing pygame and creating a visible window
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Space Voyager")
clock = pg.time.Clock()

# game loop (while loop)
running = True 
while running:
    #this keeps the game running using the clock
    clock.tick(FPS)
# drawing the background screen
    screen.fill(BLACK)
pg.quit()
