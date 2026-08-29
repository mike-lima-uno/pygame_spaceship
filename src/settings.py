import pygame

# Window
WINDOW_TITLE = "Pygame (rudimentary) Spaceship - Cisso Lima App (C)"
WIDTH = 1200
HEIGHT = 800
MARGIN = 15
FPS = 60

# TODO separate colors by menu

# - - - screens - - -

# menu
MENU_TITLE = "Spaceship from Cisso Lima App (C)"
BTN_START_SIZE = (300,80)

# Colors
BACKGROUND_COLOR = (15, 20, 35)
TEXT_COLOR = (235, 235, 235)
WALL_COLOR = (80, 90, 120)

# - - - ship - - -

# Ship
SHIP_SIZE = 24
SHIP_MARGIN = 4
SHIP_COLOR = (80, 220, 255)
SHIP_OUTLINE_COLOR = (220, 250, 255)

# Movement
INITIAL_SPEED = 0
DELTA_SPEED = 0.2
ACCELERATION = DELTA_SPEED
BRAKE_AMOUNT = DELTA_SPEED
MAX_SPEED = 10

# Direction vectors - 0xy on the top-left corner
UP = pygame.Vector2(0, -1)
DOWN = pygame.Vector2(0, 1)
LEFT = pygame.Vector2(-1, 0)
RIGHT = pygame.Vector2(1, 0)

# game state
STATE_MENU = 0
STATE_PLAYING = 1
STATE_PAUSED = 2
STATE_GAMEOVER = 3
