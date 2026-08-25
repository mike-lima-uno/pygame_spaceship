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

        keys = pygame.key.get_pressed()
        if keys:
            self.handle_key_pressed(keys)

    def handle_key_down(self, key):
        if key == pygame.K_ESCAPE:
            self.running = False

        # - - - arrows - - - 
        elif key == pygame.K_UP:
            self.ship.set_direction(settings.UP)

        elif key == pygame.K_DOWN:
            self.ship.set_direction(settings.DOWN)

        elif key == pygame.K_LEFT:
            self.ship.set_direction(settings.LEFT)

        elif key == pygame.K_RIGHT:
            self.ship.set_direction(settings.RIGHT)

        # - - - command buttons - - -
        elif key == pygame.K_SPACE:
            self.ship.accelerate()

        elif key == pygame.K_b:
            self.ship.brake()

        # - - - idle - - -
        # else:
        #     pass
    
    def handle_key_pressed(self, keys):
        if keys[pygame.K_SPACE]:
            self.ship.accelerate(0.1)

        elif keys[pygame.K_b]:
            self.ship.brake(0.1)

        # - - - idle - - -
        # else:
        #     pass


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
            f"Speed: {self.ship.speed:.2f}",
            True,
            settings.TEXT_COLOR,
        )

        controls_text = self.font.render(
            "Arrows: direction   Space: accelerate   B: brake   "
            f"Max. Speed: {settings.MAX_SPEED:.0f}   Esc: quit",
            True,
            settings.TEXT_COLOR,
        )

        self.screen.blit(speed_text, (settings.MARGIN, settings.MARGIN))
        self.screen.blit(
            controls_text,
            (settings.MARGIN, settings.HEIGHT - 2 * settings.MARGIN),
        )

        pygame.display.flip()

    def run(self):
        """while self.running: play, else: quit"""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()

            self.clock.tick(settings.FPS)

        pygame.quit()
