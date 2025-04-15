from pathlib import Path
from typing import Literal

import pygame

from core.types import Cordinates, Thickness

ROOT = Path(__file__).parent.parent


SESSION_FILE = ROOT / ".session.json"


# Constants for the components

SIZE_MAP: dict[Literal["sm", "md", "lg"], tuple[Cordinates, Thickness]] = {
    "sm": ((100, 30), 2),
    "md": ((150, 40), 3),
    "lg": ((200, 50), 4),
}

Variation_MAP: dict[
    Literal["standard", "primary", "secondary", "outline"], dict[str, pygame.color.Color]
] = {
    "standard": {"bg": (255, 255, 255), "text": (0, 0, 0), "border": (0, 0, 0)},
    "primary": {"bg": (0, 0, 255), "text": (255, 255, 255), "border": (0, 0, 0)},
    "secondary": {"bg": (0, 255, 0), "text": (255, 255, 255), "border": (0, 0, 0)},
    "outline": {"bg": (255, 255, 255), "text": (0, 0, 0), "border": (0, 0, 0)},
}
