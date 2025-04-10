import pygame

from core.config import settings
from core.constants import MAP_MAGNITUDE, PIXEL_LENGHT
from core.models.player import Player

pygame.display.init()

image_idle = pygame.image.load("temporary_assets/sprites/temporary_player/Sprites/IDLE.png")
image_run = pygame.image.load("temporary_assets/sprites/temporary_player/Sprites/RUN.png")
image_attack = pygame.image.load("temporary_assets/sprites/temporary_player/Sprites/ATTACK1.png")

center_aling = ((settings.width - MAP_MAGNITUDE[0]) // 2, (settings.height - MAP_MAGNITUDE[1]) // 2)
ini_pos = [0, 0]
ini_pos = [ini_pos[0] * PIXEL_LENGHT + center_aling[0], ini_pos[1] * PIXEL_LENGHT + center_aling[1]]
ini_pos = [ini_pos[0], ini_pos[1] - 20]


player1 = Player(ini_pos, (image_idle, image_run, image_attack), (10, 16, 7))
