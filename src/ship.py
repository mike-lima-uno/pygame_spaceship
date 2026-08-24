import pygame

from . import settings


class Ship:
    def __init__(self, x, y):
        self.position = pygame.Vector2(x, y)

        # The ship initially points to the right.
        self.direction = settings.RIGHT.copy()

        # Speed is always non-negative.
        self.speed = settings.INITIAL_SPEED

    def set_direction(self, direction):
        """Change direction immediately, without inertia."""
        if direction.length_squared() > 0:
            self.direction = direction.normalize()

    def accelerate(self):
        """Increase speed up to the configured maximum."""
        self.speed = min(
            self.speed + settings.ACCELERATION,
            settings.MAX_SPEED,
        )

    def brake(self):
        """Reduce speed without allowing it to become negative."""
        self.speed = max(
            self.speed - settings.BRAKE_AMOUNT,
            0,
        )

    def update(self):
        movement = self.direction * self.speed
        self.position += movement

        self.keep_inside_window()

    def keep_inside_window(self):
        """Prevent the ship from crossing the window boundaries."""
        minimum_x = settings.SHIP_SIZE + settings.SHIP_MARGIN
        maximum_x = settings.WIDTH - settings.SHIP_SIZE - settings.SHIP_MARGIN
        minimum_y = settings.SHIP_SIZE + settings.SHIP_MARGIN
        maximum_y = settings.HEIGHT - settings.SHIP_SIZE - settings.SHIP_MARGIN

        hit_wall = False

        if self.position.x < minimum_x:
            self.position.x = minimum_x
            hit_wall = True
        elif self.position.x > maximum_x:
            self.position.x = maximum_x
            hit_wall = True

        if self.position.y < minimum_y:
            self.position.y = minimum_y
            hit_wall = True
        elif self.position.y > maximum_y:
            self.position.y = maximum_y
            hit_wall = True

        # Stop at the wall instead of passing through it.
        if hit_wall:
            self.speed = 0

    def get_polygon(self):
        """Create a triangular polygon pointing in the current direction."""
        forward = self.direction
        perpendicular = pygame.Vector2(-forward.y, forward.x)

        nose = (
            self.position
            + forward * settings.SHIP_SIZE
        )

        rear_left = (
            self.position
            - forward * settings.SHIP_SIZE * 0.65
            + perpendicular * settings.SHIP_SIZE * 0.65
        )

        rear_right = (
            self.position
            - forward * settings.SHIP_SIZE * 0.65
            - perpendicular * settings.SHIP_SIZE * 0.65
        )

        return [nose, rear_left, rear_right]

    def draw(self, screen):
        polygon = self.get_polygon()

        pygame.draw.polygon(
            screen,
            settings.SHIP_COLOR,
            polygon,
        )

        pygame.draw.polygon(
            screen,
            settings.SHIP_OUTLINE_COLOR,
            polygon,
            width=2,
        )
