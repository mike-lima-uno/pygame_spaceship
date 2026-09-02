import pygame
from . import settings


class Ship:

    def __init__(self, x, y):
        """define the inital position, direction and speed of the ship"""
        if settings.DRAW_SHIP:
            self.image = pygame.image.load(settings.SHIP_IMAGE).convert_alpha()
            self.image = pygame.transform.scale(
                self.image,
                (settings.SHIP_SIZE * 2, settings.SHIP_SIZE * 2),
            )
            self.position = self.image.get_rect(
                center=(x, y)
            )
        else:
            self.position = pygame.Vector2(x, y)

        self.direction = settings.UP.copy()
        self.direction_last = self.direction.copy()
        self.speed = settings.INITIAL_SPEED
        self.destroyed = False

    def set_direction(self, direction):
        """Change direction immediately, without inertia."""
        if direction.length_squared() > 0:
            self.direction = direction.normalize()

    def accelerate(self, factor:int = 1):
        """Increase speed up to the configured maximum."""
        self.speed = min(
            self.speed + factor * settings.ACCELERATION,
            settings.MAX_SPEED,
        )

    def brake(self, factor:int = 1):
        """Reduce speed without allowing it to become negative."""
        self.speed = max(
            self.speed - factor * settings.BRAKE_AMOUNT,
            0,
        )

    def update(self):
        movement = self.direction * self.speed
        if not settings.DRAW_SHIP:
            self.position += movement
        else:
            self.position.center += movement

        self.detect_wall_collision()

    def detect_wall_collision(self):
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

            # game over condition
            self.destroyed = True

    def get_polygon(self):
        """Create a triangular polygon pointing in the current direction."""

        if settings.DRAW_SHIP: 
            return

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
        if settings.DRAW_SHIP: 
            if self.direction != self.direction_last.copy():
                cross = self.direction.cross(self.direction_last)
                if cross == 0:
                    self.image = pygame.transform.rotate(self.image, 180)
                elif cross > 0:
                    self.image = pygame.transform.rotate(self.image, 90)
                elif cross < 0:
                    self.image = pygame.transform.rotate(self.image, -90)
            screen.blit(self.image, self.position)
            self.direction_last = self.direction.copy()
            return
        
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
