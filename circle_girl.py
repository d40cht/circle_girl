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
[ 66,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 66],
[ 66,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 66],
[ 66,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 66],
[ 66,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 66],
[ 66,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 66],
[ 66,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 66],
[ 66,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 66],
[ 66,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 66],
[ 66,  0,  0,  0,  0,  0, 67, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66,  0,  0,  0,  0,  0,  0, 66],
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


def draw_sprite(screen, sprites, sprite_number, sprite_x, sprite_y):
  if sprite_number > 0:
    screen.blit(sprites[sprite_number-1], (sprite_x * SIZE, sprite_y * SIZE),
          (0, 0, SIZE, SIZE))

def draw_map(screen, sprites, map):
  screen.fill(BACKGROUND)
  width, height = map.shape
  for x in range(width):
    for y in range(height):
      draw_sprite(screen, sprites, map[y, x], x, y)


def loop(screen, font, key_events, sprites, map):
  draw_map(screen, sprites, map)


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


  clock = pygame.time.Clock()
  while True:
    events = pygame.event.get()

    # Extract the key events.
    key_events = set([e.key for e in events if e.type == KEYDOWN])

    for e in events:
      if e.type == QUIT:
        return

    # Update the screen.
    loop(screen, font, key_events, sprites, MAP)

    # Flip the display.
    pygame.display.flip()

    print('Tick')
    clock.tick(1)


if __name__ == '__main__':
  run()

