import numpy as np


def build_board(size):
    board = np.random.choice(['Empty', 'Red', 'Black'], (size, size))
    return board


def get_count(board, value):
    count = 0
    for a_list in board:
        for a_value in a_list:
            if a_value == value:
                count += 1
    return {value: count}


def change_size(size):
    return build_board(size)


if __name__ == "__main__":
    print("\nWarning: this file is not intended to be run as main")