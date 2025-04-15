from abc import ABC, abstractmethod
from collections.abc import Callable
from typing import Literal

import pygame

from core.types import Cordinates, Thickness


class BaseComponent(ABC):
    """
    Abstract base class for all components.
    """

    def __init__(
        self,
        window: pygame.Surface,
        label: str,
        position: tuple[int, int],
        variant: Literal["standar", "primary", "secondaty", "outline"] = "standard",
        size: Literal["sm", "md", "lg"] = "md",
        *,
        callback: Callable = lambda: print("Button clicked!"),
    ) -> None:
        """
        Initialize the component.

        Args:
            window (pygame.Surface): The window where the component will be drawn.
            position (tuple[int, int]): The position of the component.
            variant (str): The variant of the component.
            size (str): The size of the component.
            callback (Callable): A callback function to be executed on click.
        """
        self.label = label
        self.window = window
        self.position = position
        self.variant = variant
        self.size = size
        self.callback = callback
        self.is_focused = False
        self.dissabled = False
        self.surface = self._init_surface()
        self.rect = self.surface.get_rect(center=position)

    @abstractmethod
    def _init_surface(self) -> pygame.Surface:
        """
        Initialize the surface of the component.
        """
        surface = pygame.Surface
        ...
        NotImplementedError("Subclasses must implement this method.")
        return surface

    def _create_surface(self, size) -> pygame.Surface:
        """
        Create the surface of the component's part.
        """
        return pygame.surface.Surface(size, flags=pygame.SRCALPHA)

    def _get_color(self, surface_part: Literal["bg", "text", "border"]) -> tuple[int, int, int]:
        """
        Get the color of the component based on its part.
        """
        colors = {
            "standard": {"bg": (255, 255, 255), "text": (0, 0, 0), "border": (0, 0, 0)},
            "primary": {"bg": (0, 0, 255), "text": (255, 255, 255), "border": (0, 0, 0)},
            "secondary": {"bg": (0, 255, 0), "text": (255, 255, 255), "border": (0, 0, 0)},
            "outline": {"bg": (255, 255, 255), "text": (0, 0, 0), "border": (0, 0, 0)},
        }
        return colors[self.variant][surface_part]

    def _get_font(self) -> pygame.font.Font:
        """
        Get the font of the component.
        """

        fonts = {
            "sm": pygame.font.Font(None, 20),
            "md": pygame.font.Font(None, 30),
            "lg": pygame.font.Font(None, 40),
        }
        return fonts[self.size]

    def _get_size(self) -> tuple[Cordinates, Thickness]:
        """
        Get the size of the component.
        """

        sizes = {
            "sm": ((100, 30), 2),
            "md": ((150, 40), 3),
            "lg": ((200, 50), 4),
        }

        on_focus_size = {
            "sm": ((125, 35), 3),
            "md": ((175, 45), 4),
            "lg": ((225, 55), 5),
        }
        if self.is_focused:
            return on_focus_size[self.size]
        return sizes[self.size]

    def handle_event(self, event: pygame.event.Event) -> None:
        """
        Handle events for the component.
        """
        if self.dissabled:
            return
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.is_focused = True
                self.update()
            else:
                self.is_focused = False
                self.update()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                print("clicked")
                self.callback()

    def render(self) -> None:
        """
        Render the component.
        """
        self.window.blit(self.surface, self.rect)

    def update(self) -> None:
        """
        Update the component.
        """
        self.surface = self._init_surface()
        self.rect = self.surface.get_rect(center=self.position)
