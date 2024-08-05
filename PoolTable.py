import os

import pygame

class PoolTable(pygame.sprite.Sprite):
    def __init__(self, image_size: tuple = (600, 300)) -> None:
        super().__init__()
        image = pygame.image.load(os.path.join("Assets", "table.png")).convert_alpha()
        self.image = pygame.transform.smoothscale(image, image_size)
        self.rect = self.image.get_rect()