from abc import ABC, abstractmethod
from collections.abc import Callable
from typing import Literal

import pygame

from core.constants import FONT_SIZE_MAP, FONT_STYLES, SIZE_MAP, VARIANT_MAP
from core.types import Cordinates, Font_Path, Thickness


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
        text_type: Literal["standard", "title", "subtitle", "text"] = "standard",
        *,
        callback: Callable = lambda: print("Button clicked!"),
        order: int | None = None,
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
        self.text_type = text_type
        self.callback = callback
        self.is_focused = False
        self.is_dissabled = False
        self.order = order
        self.type = self.__class__.__name__.lower()
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
        colors = VARIANT_MAP[self.is_dissabled][self.is_focused]

        return colors[self.variant][surface_part]

    def _get_font(self, font_style: Font_Path | None = None) -> pygame.font.Font:
        """
        Get the font of the component.
        """

        font_size = FONT_SIZE_MAP[self.is_focused][self.text_type][self.size]
        font_style = FONT_STYLES[font_style]
        font = pygame.font.Font(font_style, font_size)

        return font

    def _get_size(self) -> tuple[Cordinates, Thickness]:
        """
        Get the size of the component.
        """

        sizes = SIZE_MAP[self.is_focused][self.type]

        return sizes[self.size]

    def _hover(self, event) -> None:
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.is_focused = True
                self.update()
            else:
                self.is_focused = False
                self.update()

    def _click(self, event) -> None:
        """
        Handle click events for the component.
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self._callback()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and self.is_focused:
                self._callback()

    def _handle_event(self, event: pygame.event.Event) -> None:
        ...
        return

    def _render(self) -> None:
        ...
        return

    def _callback(self) -> None:
        self.callback()

    def handle_event(self, event: pygame.event.Event) -> None:
        """
        Handle events for the component.
        """
        if self.is_dissabled:
            return
        self._handle_event(event)
        self._hover(event)
        self._click(event)

    def render(self) -> None:
        """
        Render the component.
        """
        self._render()
        self.window.blit(self.surface, self.rect)

    def update(self) -> None:
        """
        Update the component.
        """
        self.surface = self._init_surface()
        self.rect = self.surface.get_rect(center=self.position)
