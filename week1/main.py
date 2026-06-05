from constants import START_POS
from utils import clear_screen, create_grid, print_grid, is_valid_move

def main():
    player_r, player_c = START_POS
    grid = create_grid()
    message = ""

    while True:
        clear_screen()
        print_grid(grid, (player_r, player_c))
                
        if message:
            print(f"\n{message}")
            message = ""
            
        move = input().strip().upper()
        if move == 'Q':
            break
        new_r, new_c = player_r, player_c
        if move == 'W':
            new_r -= 1
        elif move == 'S':
            new_r += 1
        elif move == 'A':
            new_c -= 1
        elif move == 'D':
            new_c += 1
        else:
            message = "Invalid Input"
            continue

        if is_valid_move(new_r, new_c):
            player_r, player_c = new_r, new_c
        else:
            message = "Invalid Move"

if __name__ == "__main__":
    main()