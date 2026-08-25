import pygame

# Window
WIDTH = 1200
HEIGHT = 800
MARGIN = 15
FPS = 60
WINDOW_TITLE = "Pygame (rudimentary) Spaceship - Cisso Lima App (C)"

# Colors
BACKGROUND_COLOR = (15, 20, 35)
SHIP_COLOR = (80, 220, 255)
SHIP_OUTLINE_COLOR = (220, 250, 255)
TEXT_COLOR = (235, 235, 235)
WALL_COLOR = (80, 90, 120)

# Ship
SHIP_SIZE = 24
SHIP_MARGIN = 4

# Movement
INITIAL_SPEED = 3.0
DELTA_SPEED = 0.2
ACCELERATION = DELTA_SPEED
BRAKE_AMOUNT = DELTA_SPEED
MAX_SPEED = 10.0

# Direction vectors - 0xy on the top-left corner
UP = pygame.Vector2(0, -1)
DOWN = pygame.Vector2(0, 1)
LEFT = pygame.Vector2(-1, 0)
RIGHT = pygame.Vector2(1, 0)
