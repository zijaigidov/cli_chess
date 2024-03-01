# unit_test.py

from ..cli_chess.square import Square
from ..cli_chess.gameboard import Gameboard


def test_is_valid_square():
    assert Square.is_valid_square('e4') == True
    assert Square.is_valid_square('a9') == False
    assert Square.is_valid_square('k2') == False


def test_is_valid_initial_board():
    VALID_INITIAL_BOARD = [
        ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
        # ...
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
        ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
    ]

    gameboard = Gameboard()  # Initialize the board
    board = gameboard.get_board()

    for row in range(0, 2):
        for col in range(8):
            assert board[row][col].symbol == VALID_INITIAL_BOARD[row][col]

    for row in range(-2, 0):
        for col in range(8):
            assert board[row][col].symbol == VALID_INITIAL_BOARD[row][col]
