import os

import pygame

class Ball(pygame.sprite.Sprite):
    # number to ball types

    def __init__(self, number: int, mass: float) -> None:
        super().__init__()

        self.__number = number
        self.__ball_type = self.__determine_ball_type()
        if self.ball_type == "cue-ball":
            self.image = pygame.image.load(os.path.join("Assets", "cue_ball.png"))
        else:
            self.image = pygame.image.load(os.path.join("Assets", f"ball_{self.number}.png"))
        self.rect = self.image.get_rect()
    
    @property
    def number(self) -> int:
        return self.__number

    @property
    def ball_type(self) -> str:
        return self.__ball_type


    def __determine_ball_type(self) -> None:
        if self.number < 8:
            return "solid"
        elif self.number > 8:
            return "stripe"
        elif self.number == 8:
            return "8-ball"
        else:
            return "cue-ball"


class Triangle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load(os.path.join("Assets", "triangle.png"))
        self.rect = self.image.get_rect()