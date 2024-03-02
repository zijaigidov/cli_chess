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


def test_is_horizontal_move():
    assert MoveValidator._is_horizontal_move('a1', 'h1') == True
    assert MoveValidator._is_horizontal_move('a1', 'a1') == False
    assert MoveValidator._is_horizontal_move('a1', 'a8') == False
    assert MoveValidator._is_horizontal_move('e4', 'd5') == False


def test_is_vertical_move():
    assert MoveValidator._is_vertical_move('a1', 'a8') == True
    assert MoveValidator._is_vertical_move('a1', 'a1') == False
    assert MoveValidator._is_vertical_move('a1', 'h1') == False
    assert MoveValidator._is_vertical_move('e4', 'd5') == False


def test_is_diagonal_move():
    assert MoveValidator._is_diagonal_move('e4', 'd5') == True
    assert MoveValidator._is_diagonal_move('a1', 'h8') == True
    assert MoveValidator._is_diagonal_move('e4', 'e4') == False
    assert MoveValidator._is_diagonal_move('e4', 'c5') == False


# square.py
def test_is_valid_square():
    assert Square.is_valid_square('e4') == True
    assert Square.is_valid_square('a9') == False
    assert Square.is_valid_square('k2') == False
