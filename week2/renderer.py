import pygame
import constants as c

def draw_the_grid(screen):
    for i in range(0, c.width, c.c_w):
        pygame.draw.line(screen, c.grey, (i, 0), (i, c.height))
    for j in range(0, c.height, c.c_h):
        pygame.draw.line(screen, c.grey, (0, j), (c.width, j))

def draw_paths(screen, players):
    for p in players:
        for block in p.path:
            r = pygame.Rect(block[0] * c.c_w, block[1] * c.c_h, c.c_w, c.c_h)
            pygame.draw.rect(screen, p.color, r)

def draw_guys(screen, players):
    for p in players:
        r = pygame.Rect(p.x * c.c_w, p.y * c.c_h, c.c_w, c.c_h)
        if p.is_dead:
            dim_color = (p.color[0]//2, p.color[1]//2, p.color[2]//2)
            pygame.draw.rect(screen, dim_color, r)
        else:
            pygame.draw.rect(screen, p.color, r)