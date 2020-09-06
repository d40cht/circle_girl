import numpy as np
import pygame
from pygame.locals import (
    KEYDOWN, QUIT,
    K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE
)
import random

SIZE = 32

BACKGROUND = (64, 64, 64)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

MAP = np.array([
[ 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66],
[ 66,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 66,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 66],
[ 66,  0, 66,  0, 66, 66, 66, 66, 66, 66,  0, 66,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 66],
[ 66,  0, 66,  0, 66,  0,  0,  0,  0, 66,  0, 66,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 66],
[ 66,  0, 66,  0, 66,  0,  0,  0,  0, 66,  0, 66,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 66],
[ 66,  0, 66,  0, 66,  0,  0,  0,  0, 66,  0, 66,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 66],
[ 66,  0, 66,  0, 66,  0,  0,  0,  0, 66,  0, 66,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 66],
[ 66,  0, 66,  0, 66,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 66],
[ 66,  0,  0,  0, 66,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 66],
[ 66, 66, 66, 66, 66,  0, 67, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66,  0,  0,  0,  0,  0,  0, 66],
[ 66,  0,  0,  0,  0,  0, 67,  0,  0,  0,  0,  0,  0,  0,  0,  0, 66,  0,  0,  0,  0,  0,  0, 66],
[ 66,  0,  0,  0,  0,  0, 67,  0,  0,  0,  0,  0,  0,  0,  0,  0, 66,  0,  0,  0,  0,  0,  0, 66],
[ 66,  0,  0,  0,  0,  0, 67,  0,  0,  0,  0,  0,  0,  0,  0,  0, 66,  0,  0,  0,  0,  0,  0, 66],
[ 66,  0,  0,  0,  0,  0, 67,  0,  0,  0,  0,  1,  2,  0,  0,  0, 66,  0,  0,  0,  0,  0,  0, 66],
[ 66,  0,  0,  0,  0,  0, 67,  0,  0,  0,  0,  3,  4,  0,  0,  0, 66,  0,  0,  0,  0,  0,  0, 66],
[ 66,  0,  0,  0,  0,  0, 67,  0,  0,  0,  0,  0,  0,  0,  0,  0, 66,  0,  0,  0,  0,  0,  0, 66],
[ 66,  0,  0,  0,  0,  0, 67,  0,  0,  0,  0,  0,  0,  0,  0,  0, 66,  0,  0,  0,  0,  0,  0, 66],
[ 66,  0,  0,  0,  0,  0, 67,  0,  0,  0,  0,  0,  0,  0,  0,  0, 66,  0,  0,  0,  0,  0,  0, 66],
[ 66,  0,  0,  0,  0,  0, 66,  0,  0,  0,  0,  0,  0,  0,  0,  0, 66,  0,  0,  0,  0,  0,  0, 66],
[ 66,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 66],
[ 66,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 66],
[ 66,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 66],
[ 66,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 66],
[ 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66]
])

def round_fc(proposed_loc):
  floor = int(np.floor(float(proposed_loc) / SIZE))
  ceil = int(np.ceil(float(proposed_loc) / SIZE))

  return floor, ceil

def is_wall(value):
  return value in [66, 67]

class CircleGirl(object):
  def __init__(self, map, sprites, x, y):
    self.map = map
    self.sprites = sprites
    self.x = x * SIZE
    self.y = y * SIZE
    self.dx = 4
    self.dy = 0

  def draw(self, screen):
    screen.blit(self.sprites[0], (self.x, self.y), (0, 0, SIZE, SIZE))

  def is_clear(self, dx, dy):
    assert(not(dx != 0 and dy != 0))
    if dx != 0:
      if dx > 1:
        nx = int(np.ceil((self.x + dx) / float(SIZE)))
      else:
        nx = int(np.floor((self.x + dx) / float(SIZE)))
      floor, ceil = round_fc(self.y)
      return not (is_wall(self.map[floor, nx]) or is_wall(self.map[ceil, nx]))
    else:
      if dy > 1:
        ny = int(np.ceil((self.y + dy) / float(SIZE)))
      else:
        ny = int(np.floor((self.y + dy) / float(SIZE)))
      floor, ceil = round_fc(self.x)
      return not (is_wall(self.map[ny, floor]) or is_wall(self.map[ny, ceil]))

  def update(self, keys_pressed):
    if keys_pressed[K_RIGHT] and self.is_clear(4, 0):
      self.dx = 4
      self.dy = 0
    elif keys_pressed[K_LEFT] and self.is_clear(-4, 0):
      self.dx = -4
      self.dy = 0
    elif keys_pressed[K_DOWN] and self.is_clear(0, 4):
      self.dx = 0
      self.dy = 4
    elif keys_pressed[K_UP] and self.is_clear(0, -4):
      self.dx = 0
      self.dy = -4

    width, height = self.map.shape

    if self.is_clear(self.dx, self.dy):
      self.x = (self.x + self.dx) % (width * SIZE)
      self.y = (self.y + self.dy) % (height * SIZE)


def draw_sprite(screen, sprites, sprite_number, sprite_x, sprite_y):
  if sprite_number > 0:
    screen.blit(sprites[sprite_number-1], (sprite_x * SIZE, sprite_y * SIZE),
          (0, 0, SIZE, SIZE))


def draw_map(screen, sprites, map):
  screen.fill(BACKGROUND)
  height, width = map.shape
  for x in range(width):
    for y in range(height):
      draw_sprite(screen, sprites, map[y, x], x, y)


def loop(screen, font, keys_pressed, sprites, map, circle_girl):
  circle_girl.update(keys_pressed)
  draw_map(screen, sprites, map)
  circle_girl.draw(screen)


def load_sprites(sheet):
  sprites = []
  for y in range(0, sheet.get_height(), SIZE):
    for x in range(0, sheet.get_width(), SIZE):
      sprite = pygame.Surface([SIZE, SIZE])
      sprite.blit(sheet, (0, 0), (x, y, SIZE, SIZE))
      sprites.append(sprite)

  return sprites



def run():
  # Set up pygame.
  pygame.init()

  # And set up drawing text.
  pygame.font.init()

  # Load sprites
  sprite_sheet = pygame.image.load('circle_girl_sprites.png')

  sprites = load_sprites(sprite_sheet)


  height, width = MAP.shape

  # Set up the screen.
  screen = pygame.display.set_mode([width*SIZE, height*SIZE])

  # Choose a font.
  font = pygame.font.SysFont('Arial', 20)

  circle_girl = CircleGirl(MAP, sprites, 1, 1)


  clock = pygame.time.Clock()
  while True:
    events = pygame.event.get()

    for e in events:
      if e.type == QUIT:
        return

    # Extract the key events.
    keys_pressed = pygame.key.get_pressed()

    # Update the screen.
    loop(screen, font, keys_pressed, sprites, MAP, circle_girl)

    # Flip the display.
    pygame.display.flip()

    clock.tick(25)


if __name__ == '__main__':
  run()

