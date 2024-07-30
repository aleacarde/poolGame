import pygame

from PoolTable import PoolTable

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

DISPLAYSURFACE = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

table = PoolTable()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    DISPLAYSURFACE.blit(table.image, table.image.get_rect(center = DISPLAYSURFACE.get_rect().center))
    pygame.display.flip()
    