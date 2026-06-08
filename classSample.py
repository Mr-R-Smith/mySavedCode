import pygame, sys, random, os, math
from pygame.locals import *
os.environ["SDL_VIDEO_CENTERED"] = "1"  #centers the screen
pygame.init()
#make the game window
win = pygame.display
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
d = win.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
win.set_caption('title')

# Game Setup
clock = pygame.time.Clock()

#general set-up
background=pygame.image.load("img/background.png")
background=pygame.transform.scale(background, (800, 600))


# The main function that controls the game

    




def main () :
  looping = True
  # The main game loop
  while looping :
    d.blit(background, (0,0))
    # Get inputs



    pygame.display.update()
    pygame.display.flip()
main()
