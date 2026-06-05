import os
from constants import ROWS, COLS, empty_CHAR, player_CHAR, obstacle_CHAR, obstacles

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_grid():
    grid = [[empty_CHAR for _ in range(COLS)] for _ in range(ROWS)]
    for r, c in obstacles:
        grid[r][c] = obstacle_CHAR
    return grid

def print_grid(grid, player_pos):
    for r in range(ROWS):
        row_str = ""
        for c in range(COLS):
            if (r, c) == player_pos:
                row_str += player_CHAR + " "
            else:
                row_str += grid[r][c] + " "
        print(row_str.strip())

def is_valid_move(new_r, new_c):
    if new_r < 0 or new_r >= ROWS or new_c < 0 or new_c >= COLS:
        return False
    if (new_r, new_c) in obstacles:
        return False
    
    return True