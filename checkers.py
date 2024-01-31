import checkers
import numpy as np


def game():
    rebuild = True
    size = int(input("What size game board would you like to play?: "))
    board = checkers.build_board(size)
    while rebuild:
        print(f"\nGameboard: \n{board}\n")
        board_values = np.unique(board)
        dictionary = {}
        print("Count of each value:")
        for x in board_values:
            dictionary.update(checkers.get_count(board, x))
        for key, value in dictionary.items():
            print(f"{key}: {value}")

        change = input("\nWould you like to change the size of the board? (y/n): ")
        if change.upper() == 'Y':
            new_size = int(input("What size would you like to change the board to?: "))
            board = checkers.change_size(new_size)
        else:
            print("Thank you for playing!")
            rebuild = False


if __name__ == '__main__':
    game()
