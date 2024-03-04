# test_move_validator.py

from ..cli_chess.gameboard import Gameboard
from ..cli_chess.move_validator import MoveValidator


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


def test_is_valid_knight_path():
    assert MoveValidator._is_valid_knight_path('e4', 'c5') == True
    assert MoveValidator._is_valid_knight_path('e4', 'f2') == True
    assert MoveValidator._is_valid_knight_path('e4', 'c6') == False
    assert MoveValidator._is_valid_knight_path('e4', 'h4') == False


def test_is_valid_bishop_path():
    board_state = [
        ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
        ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
        ['   ', '   ', '   ', '   ', '   ', 'P_b', '   ', '   '],
        ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
        ['   ', '   ', '   ', 'B_w', '   ', '   ', '   ', '   '],
        ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
        ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
        ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
    ]
    gameboard = Gameboard(board_state)

    assert MoveValidator._is_valid_bishop_path('d4', 'f6', gameboard) == True
    assert MoveValidator._is_valid_bishop_path('d4', 'a7', gameboard) == True
    assert MoveValidator._is_valid_bishop_path('d4', 'g1', gameboard) == True

    assert MoveValidator._is_valid_bishop_path('d4', 'f4', gameboard) == False
    assert MoveValidator._is_valid_bishop_path('d4', 'b7', gameboard) == False
    assert MoveValidator._is_valid_bishop_path('d4', 'g7', gameboard) == False
