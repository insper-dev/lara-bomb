import pygame

from client.components import Components
from client.scenes.base import BaseScene


class StartScene(BaseScene):
    def __init__(self, app) -> None:
        super().__init__(app)
        self.app = app
        self.order = [0, 1, 2]
        self.components = [
            Components.button(
                self.app.screen,
                label="Entrar",
                position=(self.app.screen_center[0], self.app.screen_center[1] * 1.25),
                variant="standard",
                size="lg",
                callback=lambda: print("Start button clicked"),
                order=self.order[1],
            ),
            Components.button(
                self.app.screen,
                label="Sair",
                position=(self.app.screen_center[0], self.app.screen_center[1] * 1.5),
                variant="outline",
                size="lg",
                callback=lambda: print("Exit button clicked"),
                order=self.order[2],
            ),
            Components.text_area(
                self.app.screen,
                label="BombDuni",
                position=(self.app.screen_center[0], self.app.screen_center[1] * 0.6),
                variant="standard",
                size="lg",
                text_type="title",
                order=None,
            ),
            Components.input(
                self.app.screen,
                label="input",
                position=self.app.screen_center,
                variant="standard",
                size="lg",
                text_type="standard",
                order=self.order[0],
            ),
        ]

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.QUIT:
            self.app.running = False

        # Changing the focus of the button
        self.changing_focus(event)

    def render(self) -> None:
        self.app.screen.fill((1, 5, 68))

    def changing_focus(self, event) -> None:
        """
        Change the focus of the button.
        """
        next_component = None
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_UP, pygame.K_DOWN]:
                for component in self.components:
                    print("all: " + str(component.order))
                    if component.is_focused:
                        print("focused: " + str(component.order))
                        component.is_focused = False
                        component.update()
                        if component.type == "input":
                            if component.active:
                                next_component = component.order
                                break
                        if event.key in [pygame.K_UP]:
                            next_component = component.order - 1
                            break
                        elif event.key in [pygame.K_DOWN]:
                            next_component = component.order + 1
                            break
                print("next: " + str(next_component) + "\n")
                if next_component is None or next_component > len(self.order) - 1:
                    next_component = 0
                elif next_component == -1:
                    next_component = self.order[-1]
                print("next: " + str(next_component) + "\n")

        if isinstance(next_component, int):
            print("entered")
            for component in self.components:
                if component.order == next_component:
                    component.is_focused = True
                    component.update()

        # TODO: define color constants at core.constants
