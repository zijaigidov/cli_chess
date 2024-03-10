# test_move_validator.py

from ..cli_chess.gameboard import Gameboard
from ..cli_chess import move_validator


def test_get_file_distance():
    assert move_validator._get_file_dist('a', 'h') == 7
    assert move_validator._get_file_dist('h', 'a') == 7


def test_get_rank_distance():
    assert move_validator._get_rank_dist('1', '8') == 7
    assert move_validator._get_rank_dist('8', '1') == 7


def test_is_horizontal_move():
    assert move_validator._is_horizontal_move('a1', 'h1')
    assert not move_validator._is_horizontal_move('a1', 'a1')
    assert not move_validator._is_horizontal_move('a1', 'a8')
    assert not move_validator._is_horizontal_move('e4', 'd5')


def test_is_vertical_move():
    assert move_validator._is_vertical_move('a1', 'a8')
    assert not move_validator._is_vertical_move('a1', 'a1')
    assert not move_validator._is_vertical_move('a1', 'h1')
    assert not move_validator._is_vertical_move('e4', 'd5')


def test_is_diagonal_move():
    assert move_validator._is_diagonal_move('e4', 'd5')
    assert move_validator._is_diagonal_move('a1', 'h8')
    assert not move_validator._is_diagonal_move('e4', 'e4')
    assert not move_validator._is_diagonal_move('e4', 'c5')


def test_is_valid_knight_path():
    assert move_validator._is_valid_knight_path('e4', 'c5')
    assert move_validator._is_valid_knight_path('e4', 'f2')
    assert not move_validator._is_valid_knight_path('e4', 'c6')
    assert not move_validator._is_valid_knight_path('e4', 'h4')


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

    assert move_validator._is_valid_bishop_path('d4', 'f6', gameboard)
    assert move_validator._is_valid_bishop_path('d4', 'a7', gameboard)
    assert move_validator._is_valid_bishop_path('d4', 'g1', gameboard)

    assert not move_validator._is_valid_bishop_path('d4', 'f4', gameboard)
    assert not move_validator._is_valid_bishop_path('d4', 'b7', gameboard)
    assert not move_validator._is_valid_bishop_path('d4', 'g7', gameboard)


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

    assert move_validator._is_valid_rook_path('d4', 'd8', gameboard)
    assert move_validator._is_valid_rook_path('d4', 'a4', gameboard)
    assert move_validator._is_valid_rook_path('d4', 'g4', gameboard)

    assert not move_validator._is_valid_rook_path('d4', 'e3', gameboard)
    assert not move_validator._is_valid_rook_path('d4', 'h4', gameboard)


def test_is_valid_queen_path():
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

    assert move_validator._is_valid_queen_path('d4', 'd8', gameboard)
    assert move_validator._is_valid_queen_path('d4', 'g4', gameboard)
    assert move_validator._is_valid_queen_path('d4', 'g7', gameboard)

    assert not move_validator._is_valid_queen_path('d4', 'e1', gameboard)
    assert not move_validator._is_valid_queen_path('d4', 'h8', gameboard)


def test_is_valid_king_path():
    board_state = [
        ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
        ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
        ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
        ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
        ['   ', '   ', '   ', 'K_w', 'P_b', '   ', '   ', '   '],
        ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
        ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
        ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
    ]
    gameboard = Gameboard(board_state)

    assert move_validator._is_valid_king_path('d4', 'c4')
    assert move_validator._is_valid_king_path('d4', 'd5')
    assert move_validator._is_valid_king_path('d4', 'c5')
    assert move_validator._is_valid_king_path('d4', 'c4')

    assert not move_validator._is_valid_king_path('d4', 'd6')
    assert not move_validator._is_valid_king_path('d4', 'f2')
