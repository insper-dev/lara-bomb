import pygame

from client.scenes.base import BaseScene
from core.constants import BLACK, BLUE, MAP_MAGNITUDE, PIXEL_LENGHT, RED, WHITE
from core.models.__init__ import player1


class StartScene(BaseScene):
    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.QUIT:
            self.app.running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("enter")
        player1.get_event(event)

    def render(self) -> None:
        self.app.screen.fill(BLACK)
        player1.update()
        self.draw()

        # TODO: define color constants at core.constants

    def generate_map(
        self,
        screen_size: tuple[int, int],
        size: tuple[int, int] = [7, 4],
        pixel_lengh: int = 64,
        external_walls_color: tuple[int, int, int] = BLUE,
        ground_color: tuple[int, int, int] = RED,
    ) -> None:
        """
        Only for tests
        """
        align = ((screen_size[0] - MAP_MAGNITUDE[0]) // 2, (screen_size[1] - MAP_MAGNITUDE[1]) // 2)
        for y in range(0, size[1] + 2):
            for x in range(0, size[0] + 2):
                if y in [0, size[1] + 1]:
                    pygame.draw.rect(
                        self.app.screen,
                        external_walls_color,
                        (
                            x * pixel_lengh + 1 + align[0],
                            y * pixel_lengh + 1 + align[1],
                            pixel_lengh - 2,
                            pixel_lengh - 2,
                        ),
                    )
                elif y in range(1, size[1] + 1) and x in [0, size[0] + 1]:
                    pygame.draw.rect(
                        self.app.screen,
                        external_walls_color,
                        (
                            x * pixel_lengh + 1 + align[0],
                            y * pixel_lengh + 1 + align[1],
                            pixel_lengh - 2,
                            pixel_lengh - 2,
                        ),
                    )
                else:
                    pygame.draw.rect(
                        self.app.screen,
                        ground_color,
                        (
                            x * pixel_lengh + 1 + align[0],
                            y * pixel_lengh + 1 + align[1],
                            pixel_lengh - 2,
                            pixel_lengh - 2,
                        ),
                    )

    def draw(self) -> None:
        self.generate_map(
            self.app.screen.get_size(), size=(15, 10), pixel_lengh=PIXEL_LENGHT, ground_color=WHITE
        )
        player1.draw(self.app.screen)
