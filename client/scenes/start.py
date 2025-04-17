import pygame

from client.components import BaseComponent, Button, Input, State, TextArea
from client.scenes.base import BaseScene


class StartScene(BaseScene):
    def __init__(self, app) -> None:
        super().__init__(app)
        self.app = app
        self.active_button = 0
        self.components: list[BaseComponent] = [
            TextArea(
                self.app.screen,
                position=(self.app.screen_center[0], self.app.screen_center[1] * 0.6),
                label="BombDuni",
                variant="standard",
                size="lg",
                text_type="title",
            ),
            Input(
                self.app.screen,
                label="Haja paz",
                position=(self.app.screen_center[0], self.app.screen_center[1]),
                size="lg",
            ),
            State(
                self.app.screen,
                position=(self.app.screen_center[0], self.app.screen_center[1] * 1.25),
                label="Entrar",
                variant="standard",
                size="lg",
                callback=lambda: print("Start button clicked"),
            ),
            Button(
                self.app.screen,
                position=(self.app.screen_center[0], self.app.screen_center[1] * 1.5),
                label="Sair",
                variant="outline",
                size="lg",
                callback=lambda: print("Exit button clicked"),
            ),
        ]

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.QUIT:
            self.app.running = False

        # Changing the focus of the button
        self.changing_focus(event)

    def render(self) -> None:
        self.app.screen.fill((1, 5, 68))

    def changing_focus(self, event: pygame.event.Event) -> None:
        """
        Change the focus of the button.
        """
        moviment = {pygame.K_UP: -1, pygame.K_DOWN: 1}
        if event.type == pygame.KEYDOWN:
            if event.key in moviment:
                self.active_button = (self.active_button + moviment[event.key]) % len(
                    self.components
                )
                for i, component in enumerate(self.components):
                    component.is_focused = i == self.active_button
                    print(f"{component.type=}; {component.is_focused}")
