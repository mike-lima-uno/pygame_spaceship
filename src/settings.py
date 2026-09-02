import pygame
from pathlib import Path

# Window
WINDOW_TITLE = "Pygame (rudimentary) Spaceship - Cisso Lima App (C)"
WIDTH = 1200
HEIGHT = 800
MARGIN = 15
FPS = 60

# TODO separate colors by menu

# - - - screens - - -

# Colors
BACKGROUND_COLOR = (15, 20, 35)
TEXT_COLOR = (235, 235, 235)
WALL_COLOR = (80, 90, 120)
GAMEOVER_COLOR = (255, 255, 0)
PAUSE_COLOR = (255, 255, 0)

# menu
MENU_TITLE = "Spaceship"
BTN_START_SIZE = (300,80)

# paused
PAUSED_TITLE = "Paused"
PAUSED_MESSAGE = "Press P to continue."

# game over
GAMEOVER_TITLE = "Game Over"
GAMEOVER_MESSAGE = "Press ENTER to restart."

# - - - ship - - -

# DRAW_SHIP indicates whether to draw the ship (true) 
# or triangle (false) on the screen.
DRAW_SHIP = True

BASE_DIR = Path(__file__).resolve().parent.parent
SHIP_IMAGE = BASE_DIR / "assets" / "spaceship32x32_up.png"


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
