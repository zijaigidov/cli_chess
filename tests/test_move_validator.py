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
    assert MoveValidator._is_horizontal_move('a1', 'h1')
    assert not MoveValidator._is_horizontal_move('a1', 'a1')
    assert not MoveValidator._is_horizontal_move('a1', 'a8')
    assert not MoveValidator._is_horizontal_move('e4', 'd5')


def test_is_vertical_move():
    assert MoveValidator._is_vertical_move('a1', 'a8')
    assert not MoveValidator._is_vertical_move('a1', 'a1')
    assert not MoveValidator._is_vertical_move('a1', 'h1')
    assert not MoveValidator._is_vertical_move('e4', 'd5')


def test_is_diagonal_move():
    assert MoveValidator._is_diagonal_move('e4', 'd5')
    assert MoveValidator._is_diagonal_move('a1', 'h8')
    assert not MoveValidator._is_diagonal_move('e4', 'e4')
    assert not MoveValidator._is_diagonal_move('e4', 'c5')


def test_is_valid_knight_path():
    assert MoveValidator._is_valid_knight_path('e4', 'c5')
    assert MoveValidator._is_valid_knight_path('e4', 'f2')
    assert not MoveValidator._is_valid_knight_path('e4', 'c6')
    assert not MoveValidator._is_valid_knight_path('e4', 'h4')


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

    assert MoveValidator._is_valid_bishop_path('d4', 'f6', gameboard)
    assert MoveValidator._is_valid_bishop_path('d4', 'a7', gameboard)
    assert MoveValidator._is_valid_bishop_path('d4', 'g1', gameboard)

    assert not MoveValidator._is_valid_bishop_path('d4', 'f4', gameboard)
    assert not MoveValidator._is_valid_bishop_path('d4', 'b7', gameboard)
    assert not MoveValidator._is_valid_bishop_path('d4', 'g7', gameboard)


def test_is_valid_rook_path():
    board_state = [
        ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
        ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
        ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
        ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
        ['   ', '   ', '   ', 'R_w', '   ', '   ', 'P_b', '   '],
        ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
        ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
        ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
    ]
    gameboard = Gameboard(board_state)

    assert MoveValidator._is_valid_rook_path('d4', 'd8', gameboard)
    assert MoveValidator._is_valid_rook_path('d4', 'a4', gameboard)
    assert MoveValidator._is_valid_rook_path('d4', 'g4', gameboard)

    assert not MoveValidator._is_valid_rook_path('d4', 'e3', gameboard)
    assert not MoveValidator._is_valid_rook_path('d4', 'h4', gameboard)


def test_is_valid_rook_path():
    board_state = [
        ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
        ['   ', '   ', '   ', '   ', '   ', '   ', 'P_b', '   '],
        ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
        ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
        ['   ', '   ', '   ', 'Q_w', '   ', '   ', '   ', '   '],
        ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
        ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
        ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
    ]
    gameboard = Gameboard(board_state)

    assert MoveValidator._is_valid_queen_path('d4', 'd8', gameboard)
    assert MoveValidator._is_valid_queen_path('d4', 'g4', gameboard)
    assert MoveValidator._is_valid_queen_path('d4', 'g7', gameboard)

    assert not MoveValidator._is_valid_queen_path('d4', 'e1', gameboard)
    assert not MoveValidator._is_valid_queen_path('d4', 'h8', gameboard)
