import pygame
import sys

from . import settings
from .ship import Ship


class Game:
    
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode(
            (settings.WIDTH, settings.HEIGHT),
            pygame.FULLSCREEN
        )
        # self.screen = pygame.display.set_mode(
        #     (settings.WIDTH, settings.HEIGHT),
        # )

        pygame.display.set_caption(settings.WINDOW_TITLE)

        self.clock = pygame.time.Clock()

        self.font = pygame.font.Font(None, 40)
        self.title_font = pygame.font.Font(None, 100)
        self.small_font = pygame.font.Font(None, 28)

        self.running = True
        self.state = settings.STATE_MENU

    def start_game(self):

        self.ship = Ship(
            settings.WIDTH // 2,
            settings.HEIGHT // 2,
        )
        
        self.state = settings.STATE_PLAYING

    def draw_centered_text(self, text, font, color, y):
        image = font.render(text, True, color)
        rectangle = image.get_rect(
            center=(settings.WIDTH // 2, y)
        )
        self.screen.blit(image, rectangle)

    def handle_events(self):
        """get inputs from player and pass it according to game state."""

        for event in pygame.event.get():

            # works on every state
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False

            # conditions for state menu
            elif self.state == settings.STATE_MENU and (
                event.type == pygame.KEYDOWN
                and event.key in (pygame.K_KP_ENTER, pygame.K_RETURN)
            ):
                self.start_game()

            # event handler for pause
            elif self.state == settings.STATE_PAUSED and (
                event.type == pygame.KEYDOWN
                and event.key == pygame.K_p
            ):
                self.state = settings.STATE_PLAYING

            # game over state
            elif self.state == settings.STATE_GAMEOVER and (
                event.type == pygame.KEYDOWN
                and event.key in (pygame.K_KP_ENTER, pygame.K_RETURN)
            ):
                self.state = settings.STATE_MENU

            # event handler for playing
            elif (
                self.state == settings.STATE_PLAYING 
                and event.type == pygame.KEYDOWN
            ):
                if event.key == pygame.K_p:
                    self.state = settings.STATE_PAUSED
                else:
                    self.handle_playing_keydown(event.key)

        # event handler for playing when holding keys down
        if self.state == settings.STATE_PLAYING:
            keys = pygame.key.get_pressed()
            if keys:
                self.handle_playing_key_pressed(keys)

    def handle_playing_keydown(self, key):
        """supports handle_events when a key downs"""

        # - - - arrows - - - 
        if key == pygame.K_UP:
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
    
    def handle_playing_key_pressed(self, keys):
        """supports handle_events when a key is hold pressed.
        accel. / brake factor means it effects a factor of keydown a loop"""

        if keys[pygame.K_SPACE]:
            self.ship.accelerate(0.5)

        elif keys[pygame.K_b]:
            self.ship.brake(0.5)

        # - - - idle - - -
        # else:
        #     pass

    def update(self):
        """updates the variables when playing, else ignore."""

        if self.state == settings.STATE_PLAYING:
            self.ship.update()

            if self.ship.is_dead:
                self.state = settings.STATE_GAMEOVER

    def draw(self):
        if self.state == settings.STATE_MENU:
            self.draw_menu()

        elif  self.state == settings.STATE_PLAYING:
            self.draw_playing()

        elif  self.state == settings.STATE_PAUSED:
            self.draw_pause()

        elif  self.state == settings.STATE_GAMEOVER:
            self.draw_gameover()

    def draw_menu(self):
        """supports draw: menu initial screen."""

        self.screen.fill(settings.BACKGROUND_COLOR)

        # game title    
        self.draw_centered_text(
            settings.MENU_TITLE,
            self.title_font,
            settings.TEXT_COLOR,
            settings.HEIGHT // 4,
        )

        self.draw_centered_text(
            "Press ENTER to start",
            self.font,
            settings.TEXT_COLOR,
            settings.HEIGHT // 2,
        )

        # Instructions under the button
        instructions = [
            "Arrow keys: Change direction",
            "Space: Accelerate / B: Brake",
            "P: Pause",
            "ESC: Quit",
        ]

        
        len_instr = len(instructions)
        first_instruction_y = self.screen.get_height() \
            - len_instr * 35 \
            - len_instr * self.small_font.get_height()

        for index, instruction in enumerate(instructions):
            self.draw_centered_text(
                instruction,
                self.small_font,
                settings.TEXT_COLOR,
                first_instruction_y + index * 35,
            )


        pygame.display.flip()

    def draw_playing(self):
        """supports draw: draw the playing screen."""
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

        self.screen.blit(speed_text, (settings.MARGIN, settings.MARGIN))
        
        pygame.display.flip()

    def draw_pause(self):
        """supports draw: draw the paused screen."""
        self.screen.fill(settings.BACKGROUND_COLOR)

        self.draw_centered_text(
            settings.PAUSED_TITLE,
            self.title_font,
            settings.PAUSE_COLOR,
            settings.HEIGHT // 2,
        )

        self.draw_centered_text(
            settings.PAUSED_MESSAGE,
            self.small_font,
            settings.TEXT_COLOR,
            settings.HEIGHT // 2 + self.title_font.get_height(),
        )

        pygame.display.flip()

    def draw_gameover(self):
        """supports draw: draw the game over screen."""
        
        self.screen.fill(settings.BACKGROUND_COLOR)

        # game title    
        self.draw_centered_text(
            settings.GAMEOVER_TITLE,
            self.title_font,
            settings.GAMEOVER_COLOR,
            settings.HEIGHT // 2,
        )

        self.draw_centered_text(
            settings.GAMEOVER_MESSAGE,
            self.small_font,
            settings.TEXT_COLOR,
            settings.HEIGHT // 2 + self.title_font.get_height(),
        )

        pygame.display.flip()

    def run(self):
        """while self.running: play, else: quit.
        BE CAREFUL: running ISN'T playing. 
        running means ON, playing is a game state."""

        while self.running:
            self.handle_events()

            if self.state == settings.STATE_PLAYING:
                self.update()

            self.draw()

            self.clock.tick(settings.FPS)


        pygame.quit()
