import pygame

from client.components import Components
from client.scenes.base import BaseScene


class StartScene(BaseScene):
    def __init__(self, app) -> None:
        super().__init__(app)
        self.components = [
            Components.button(
                self.app.screen,
                label="Start",
                position=self.app.screen_center,
                variant="standard",
                size="lg",
                callback=lambda: print("Start button clicked"),
            ),
        ]

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.QUIT:
            self.app.running = False

    def render(self) -> None:
        font = pygame.font.SysFont(None, 80)
        self.app.screen.fill((255, 0, 0))

        # TODO: define color constants at core.constants
        text = font.render("Welcome", True, (255, 255, 255))
        text_rect = text.get_rect(center=self.app.screen_center)

        self.app.screen.blit(text, text_rect)
