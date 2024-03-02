# unit_test.py

from ..cli_chess.gameboard import Gameboard
from ..cli_chess.move_validator import MoveValidator
from ..cli_chess.square import Square


# gameboard.py
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


# move_validator.py
def test_get_file_distance():
    assert MoveValidator._get_file_distance('a', 'h') == 7
    assert MoveValidator._get_file_distance('h', 'a') == 7


def test_get_rank_distance():
    assert MoveValidator._get_rank_distance('1', '8') == 7
    assert MoveValidator._get_rank_distance('8', '1') == 7


# square.py
def test_is_valid_square():
    assert Square.is_valid_square('e4') == True
    assert Square.is_valid_square('a9') == False
    assert Square.is_valid_square('k2') == False
