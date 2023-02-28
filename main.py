import pygame
from pygame.locals import *
import sys
import random
import colorswatch as cs

from tkinter import *
from tkinter import messagebox
Tk().wm_withdraw() 

class GameMaster:
  def __init__(self):
    self.screen_size = (600, 400)
    pygame.init()
    self.screen = pygame.display.set_mode(self.screen_size)
    self.maze = Maze(self.screen_size)
    self.maze.make()
    
  def main(self):  
    while True:
      self.draw()
      pygame.display.update()
      self.event()
      
  def draw(self):
    self.screen.fill(cs.black["pygame"])
    self.maze.draw(self.screen)

  def event(self):
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
      if event.type == KEYDOWN:
        self.maze.update(event.key)

class Maze():
  def __init__(self, screen_size):
    self.tile_size = 19
    self.maze_width = int(screen_size[0] / self.tile_size)
    self.maze_height = int(screen_size[1] / self.tile_size)
    self.maze = []
    self.tbl = [[0, -1], [1, 0], [0, 1], [-1, 0]]
    self.maze_color = [cs.white["pygame"], cs.brown["pygame"], cs.yellow["pygame"]]
    self.player = Player(self.maze_width - 2, self.maze_height - 2)
  
  def make(self):
    self.maze = []
    for y in range(self.maze_height):
      row = []
      for x in range(self.maze_width):
        if x == 0 or x == self.maze_width - 1 or y == 0 or y == self.maze_height - 1:
          row.append(1)
        else:
          row.append(0)
      self.maze.append(row)
    for y in range(2, self.maze_height - 2):
      for x in range(2, self.maze_width - 2):
        if x % 2 == 0 and y % 2 == 0:
          r = random.randint(0, 3)
          self.maze[y][x] = 1
          self.maze[y + self.tbl[r][1]][x + self.tbl[r][0]] = 1
    self.maze[1][1] = 2 # goal
    
  def draw(self, screen):
    for y in range(self.maze_height):
      for x in range(self.maze_width):
        v = self.maze[y][x]
        x_cor = self.tile_size * x
        y_cor = self.tile_size * y
        pygame.draw.rect(
          surface = screen,
          color = self.maze_color[v],
          rect = (
            x_cor,
            y_cor,
            self.tile_size,
            self.tile_size
          ),
        )
    self.player.draw(screen, self.tile_size)
    
  def update(self, key):
    if self.player.update(key, self.maze) == "end":
      self.make()
      self.player.__init__(self.maze_width - 2, self.maze_height - 2)
    
class Player:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    
  def draw(self, screen, tile_size):
    pygame.draw.circle(
      surface = screen,
      color = cs.red["pygame"],
      center = (
        self.x * tile_size + 0.5 * tile_size,
        self.y * tile_size + 0.5 * tile_size,
      ),
      radius = 7,
    )
  
  def update(self, key, maze):
    cx, cy = self.x, self.y
    if key == K_LEFT:
      self.x -= 1
    elif key == K_RIGHT:
      self.x += 1
    elif key == K_UP:
      self.y -= 1
    elif key == K_DOWN:
      self.y += 1
    if maze[self.y][self.x] == 2:
      messagebox.showinfo("ゴール", "宝を見つけた！")
      return "end"
    if maze[self.y][self.x] != 0:
      self.x, self.y = cx, cy
    return "continue"
    
# main
if __name__ == "__main__":
  gm = GameMaster()
  gm.main()