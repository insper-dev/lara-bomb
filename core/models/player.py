import pygame

from core.constants import PIXEL_LENGHT


class Player:
    def __init__(self, pos: list[int, int], image, number_of_sprites: int) -> None:
        pygame.init()
        self.pos = pos
        self.sprites = {
            "__sprites_idle": self.__break_image(image[0], number_of_sprites[0]),
            "__sprites_run": self.__break_image(image[1], number_of_sprites[1]),
            "__sprites_attack": self.__break_image(image[2], number_of_sprites[2]),
        }
        self.__current_sprites: list = self.sprites["__sprites_idle"]
        self.sprite_index = 0
        self.__frame_animation = pygame.time.Clock()
        self.__frame_counter = 0
        self.__moviment_counter = 0
        self.__animation_state = "dynamic"
        self.vel = 2
        self.direction = None

    def __break_image(self, image, number_of_sprites: int) -> list:
        sprites = []
        sprite_width = image.get_width() // number_of_sprites
        sprite_height = image.get_height()
        for i in range(number_of_sprites):
            sprite = pygame.Surface((sprite_width, sprite_height), pygame.SRCALPHA)
            sprite.blit(image, (0, 0), (sprite_width * i, 0, sprite_width, sprite_height))
            sprites.append(sprite)

        return sprites

    def draw(self, window) -> None:
        sprite = self.__sprite_animate(self.__current_sprites)
        if self.direction == "left":
            sprite = pygame.transform.flip(sprite, True, False)

        window.blit(sprite, tuple(self.pos))

    def get_event(self, event) -> None:
        self._get_direction(event)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and self.__animation_state == "dynamic":
                print("enter")
                self.__animation_state = "static"
                self.__current_sprites = self.sprites["__sprites_attack"]
                self.sprite_index = 0

    def update(self) -> None:
        time_passed = self.__frame_animation.tick()
        self.__frame_counter += time_passed

        if self.__animation_state == "dynamic":
            if self.direction is None:
                self.__current_sprites = self.sprites["__sprites_idle"]
            else:
                self.__current_sprites = self.sprites["__sprites_run"]

        print(self.__animation_state)

        self.__move()

    def _get_direction(self, event) -> None:
        if event.type == pygame.KEYDOWN:
            if self.direction is None:
                if event.key == pygame.K_w:
                    self.direction = "up"
                elif event.key == pygame.K_a:
                    self.direction = "left"
                elif event.key == pygame.K_s:
                    self.direction = "donw"
                elif event.key == pygame.K_d:
                    self.direction = "right"

    def __move(self) -> None:
        if self.__moviment_counter < PIXEL_LENGHT and self.direction is not None:
            match self.direction:
                case "up":
                    self.pos[1] -= self.vel
                case "left":
                    self.pos[0] -= self.vel
                case "donw":
                    self.pos[1] += self.vel
                case "right":
                    self.pos[0] += self.vel
            self.__moviment_counter += self.vel
        else:
            self.direction = None
            self.__moviment_counter = 0

    def __sprite_animate(self, sprites) -> object:
        if self.__frame_counter > 50:
            self.sprite_index += 1
            self.__frame_counter = 0
        if self.sprite_index < len(sprites):
            return sprites[self.sprite_index]
        if self.__animation_state == "static":
            self.__animation_state = "dynamic"
            self.__current_sprites = self.sprites["__sprites_idle"]
        self.sprite_index = 0
        return sprites[self.sprite_index]
