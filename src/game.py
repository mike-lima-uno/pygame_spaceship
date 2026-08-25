import pygame

from . import settings
from .ship import Ship


class Game:
    
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode(
            (settings.WIDTH, settings.HEIGHT)
        )

        pygame.display.set_caption(settings.WINDOW_TITLE)

        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 28)

        self.ship = Ship(
            settings.WIDTH // 2,
            settings.HEIGHT // 2,
        )

        self.running = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:
                self.handle_key_down(event.key)

    def handle_key_down(self, key):
        if key == pygame.K_ESCAPE:
            self.running = False

        elif key == pygame.K_UP:
            self.ship.set_direction(settings.UP)

        elif key == pygame.K_DOWN:
            self.ship.set_direction(settings.DOWN)

        elif key == pygame.K_LEFT:
            self.ship.set_direction(settings.LEFT)

        elif key == pygame.K_RIGHT:
            self.ship.set_direction(settings.RIGHT)

        elif key == pygame.K_SPACE:
            self.ship.accelerate()

        elif key == pygame.K_b:
            self.ship.brake()

    def update(self):
        self.ship.update()

    def draw(self):
        self.screen.fill(settings.BACKGROUND_COLOR)

        # Window boundary.
        pygame.draw.rect(
            self.screen,
            settings.WALL_COLOR,
            pygame.Rect(
                0,
                0,
                settings.WIDTH,
                settings.HEIGHT,
            ),
            width=3,
        )

        self.ship.draw(self.screen)

        speed_text = self.font.render(
            f"Speed: {self.ship.speed:.2f} / {settings.MAX_SPEED:.2f}",
            True,
            settings.TEXT_COLOR,
        )

        controls_text = self.font.render(
            "Arrows: direction   Space: accelerate   "
            "B: brake   Esc: quit",
            True,
            settings.TEXT_COLOR,
        )

        self.screen.blit(speed_text, (15, 15))
        self.screen.blit(
            controls_text,
            (15, settings.HEIGHT - 35),
        )

        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()

            self.clock.tick(settings.FPS)

        pygame.quit()
