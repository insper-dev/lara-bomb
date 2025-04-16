from pathlib import Path
from typing import Literal

import pygame

from core.types import Cordinates, Thickness, comp, is_disabled, is_focused

ROOT = Path(__file__).parent.parent


SESSION_FILE = ROOT / ".session.json"

# Constants for the game

# FONT_STYLES: dict[]


# Constants for the components

SIZE_MAP: dict[
    is_focused : dict[comp : dict[Literal["sm", "md", "lg"] : tuple[Cordinates, Thickness]]]
] = {
    False: {
        "button": {
            "sm": ((100, 30), 2),
            "md": ((150, 40), 3),
            "lg": ((200, 50), 4),
        },
        "text_area": {
            "sm": ((100, 30), 2),
            "md": ((150, 40), 3),
            "lg": ((200, 50), 4),
        },
        "input": {
            "sm": ((120, 30), 2),
            "md": ((170, 40), 3),
            "lg": ((220, 50), 4),
        },
    },
    True: {
        "button": {
            "sm": ((110, 35), 3),
            "md": ((160, 45), 4),
            "lg": ((210, 55), 5),
        },
        "text area": {
            "sm": ((110, 35), 3),
            "md": ((160, 45), 4),
            "lg": ((210, 55), 5),
        },
        "input": {
            "sm": ((125, 35), 3),
            "md": ((175, 45), 4),
            "lg": ((225, 55), 5),
        },
    },
}


VARIANT_MAP: dict[
    is_disabled : dict[
        is_focused : dict[
            Literal["standard", "primary", "secondary", "outline"], dict[str, pygame.color.Color]
        ]
    ]
] = {
    False: {
        False: {
            "standard": {"bg": (1, 5, 68), "text": (243, 45, 107), "border": (255, 255, 255)},
            "primary": {"bg": (0, 0, 255), "text": (255, 255, 255), "border": (0, 0, 0)},
            "secondary": {"bg": (0, 255, 0), "text": (255, 255, 255), "border": (0, 0, 0)},
            "outline": {"bg": (255, 255, 255), "text": (0, 0, 0), "border": (0, 0, 0)},
        },
        True: {
            "standard": {"bg": (1, 5, 68), "text": (243, 255, 107), "border": (255, 255, 255)},
            "primary": {"bg": (0, 0, 255), "text": (128, 128, 128), "border": (128, 128, 128)},
            "secondary": {"bg": (0, 255, 0), "text": (128, 128, 128), "border": (128, 128, 128)},
            "outline": {"bg": (255, 255, 255), "text": (128, 128, 128), "border": (128, 128, 128)},
        },
    },
    True: {
        False: {
            "standard": {"bg": (255, 255, 255), "text": (0, 0, 0), "border": (0, 0, 0)},
            "primary": {"bg": (0, 0, 255), "text": (255, 255, 255), "border": (0, 0, 0)},
            "secondary": {"bg": (0, 255, 0), "text": (255, 255, 255), "border": (0, 0, 0)},
            "outline": {"bg": (255, 255, 255), "text": (0, 0, 0), "border": (0, 0, 0)},
        },
        True: {
            "standard": {"bg": (255, 255, 255), "text": (128, 128, 128), "border": (128, 128, 128)},
            "primary": {"bg": (0, 0, 255), "text": (128, 128, 128), "border": (128, 128, 128)},
            "secondary": {"bg": (0, 255, 0), "text": (128, 128, 128), "border": (128, 128, 128)},
            "outline": {"bg": (255, 255, 255), "text": (128, 128, 128), "border": (128, 128, 128)},
        },
    },
}

FONT_STYLES: dict[
    Literal["normal", "bold", "italic", "bold_italic"],
    tuple[str, int],
] = {
    None: None,
    "normal": "freesansbold.ttf",
    "bold": "freesansbold.ttf",
    "italic": "freesansbold.ttf",
    "bold_italic": "freesansbold.ttf",
}

FONT_SIZE_MAP: dict[
    is_focused : dict[
        Literal["standard", "title", "subtitle", "text"] : dict[Literal["sm", "md", "lg"], int]
    ]
] = {
    False: {
        "standard": {
            "sm": 20,
            "md": 24,
            "lg": 30,
        },
        "title": {
            "sm": 48,
            "md": 60,
            "lg": 72,
        },
        "subtitle": {
            "sm": 18,
            "md": 24,
            "lg": 30,
        },
        "text": {
            "sm": 16,
            "md": 20,
            "lg": 24,
        },
    },
    True: {
        "standard": {
            "sm": 22,
            "md": 26,
            "lg": 32,
        },
        "title": {
            "sm": 50,
            "md": 62,
            "lg": 74,
        },
        "subtitle": {
            "sm": 20,
            "md": 26,
            "lg": 32,
        },
        "text": {
            "sm": 18,
            "md": 22,
            "lg": 26,
        },
    },
}

# Game constants

GAME_ALPHABET_KEYS = [pygame.key.key_code(key) for key in "abcdefghijklmnopqrstuvwxyz"]
