import pygame
import sys
import constants as c
from player import Player
from game import Game
import renderer

pygame.init()
win = pygame.display.set_mode((c.width, c.height))
pygame.display.set_caption("Grid Cycles")
clock = pygame.time.Clock()

my_game = Game(c.rows, c.cols)

player1 = Player(10, c.rows // 2, 1, 0, c.red, 1)
player2 = Player(c.cols - 11, c.rows // 2, -1, 0, c.blue, 2)

my_game.add(player1)
my_game.add(player2)

play = True
while play:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            play = False
        
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_r or ev.key == pygame.K_SPACE:
                my_game.restart()

            if ev.key == pygame.K_w and player1.dy != 1:
                player1.dx = 0
                player1.dy = -1
            if ev.key == pygame.K_s and player1.dy != -1:
                player1.dx = 0
                player1.dy = 1
            if ev.key == pygame.K_a and player1.dx != 1:
                player1.dx = -1
                player1.dy = 0
            if ev.key == pygame.K_d and player1.dx != -1:
                player1.dx = 1
                player1.dy = 0

            if ev.key == pygame.K_UP and player2.dy != 1:
                player2.dx = 0
                player2.dy = -1
            if ev.key == pygame.K_DOWN and player2.dy != -1:
                player2.dx = 0
                player2.dy = 1
            if ev.key == pygame.K_LEFT and player2.dx != 1:
                player2.dx = -1
                player2.dy = 0
            if ev.key == pygame.K_RIGHT and player2.dx != -1:
                player2.dx = 1
                player2.dy = 0

    my_game.update()

    win.fill(c.black)
    renderer.draw_the_grid(win)
    renderer.draw_paths(win, my_game.people)
    renderer.draw_guys(win, my_game.people)

    pygame.display.flip()
    clock.tick(c.speed)

pygame.quit()
sys.exit()