import pygame
from pygame.locals import *
import sys
import random
import colorswatch as cs

# define variables
screen_size = (600, 400)

# define functions
def main():
  screen = init()
  while True:
    draw(screen)
    pygame.display.update()
    event(screen)
  
def init():
  pygame.init()
  return pygame.display.set_mode(screen_size)

def draw(screen):
  screen.fill(cs.black["pygame"])
  
  pygame.draw.circle(screen, cs.white["pygame"], (300, 200), 150)

def event(screen):
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()

# main
if __name__ == "__main__":
  main()