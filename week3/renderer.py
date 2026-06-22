import pygame
import numpy as np
import constants as c

def get_colors():
    m = np.zeros((256, 3), dtype=np.uint8)
    m[0] = c.black
    m[1] = c.red
    m[2] = c.blue
    m[255] = c.dim_red
    m[254] = c.dim_blue
    return m
    
color_map = get_colors()

def draw_the_grid(screen):
    for i in range(0, c.width, c.c_w):
        pygame.draw.line(screen, c.grey, (i, 0), (i, c.height))
    for j in range(0, c.height, c.c_h):
        pygame.draw.line(screen, c.grey, (0, j), (c.width, j))

def draw_paths(screen, board):
    b_bytes = board.astype(np.uint8)
    rgb = color_map[b_bytes]
    rgb = np.transpose(rgb, (1, 0, 2))
    
    surf = pygame.surfarray.make_surface(rgb)
    big_surf = pygame.transform.scale(surf, (c.width, c.height))
    screen.blit(big_surf, (0, 0))

def draw_guys(screen, players):
    for p in players:
        r = pygame.Rect(p.x * c.c_w, p.y * c.c_h, c.c_w, c.c_h)
        if p.is_dead:
            dim_color = (p.color[0]//2, p.color[1]//2, p.color[2]//2)
            pygame.draw.rect(screen, dim_color, r)
        else:
            pygame.draw.rect(screen, c.white, r)