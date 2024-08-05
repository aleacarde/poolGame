import pygame

from PoolTable import PoolTable
from TableObjects import Ball

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 400
WHITE = (255, 255, 255)

pygame.init()
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont('sans-serif', 28)

text = font.render("No Coordinate Selected", True, WHITE)
text_rect = text.get_rect()
text_rect.topleft = (0, 0)
table = PoolTable()
ball = Ball(number=16, mass=0.17)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            window.fill((0,0,0))
            text = font.render(str(mouse_pos), True, WHITE)
            text_rect = text.get_rect()
            text_rect.topleft = (0, 0)
    window.blit(table.image, table.image.get_rect(center = window.get_rect().center))
    window.blit(ball.image, ball.image.get_rect(center = window.get_rect().center))
    window.blit(text, text_rect)
    pygame.display.flip()
    