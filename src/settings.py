import pygame

# Window
WIDTH = 900
HEIGHT = 600
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
ACCELERATION = 0.25
BRAKE_AMOUNT = 0.5
MAX_SPEED = 10.0

# Direction vectors
UP = pygame.Vector2(0, -1)
DOWN = pygame.Vector2(0, 1)
LEFT = pygame.Vector2(-1, 0)
RIGHT = pygame.Vector2(1, 0)
