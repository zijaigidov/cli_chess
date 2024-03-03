# test_square.py

from ..cli_chess.square import Square


def test_is_valid_square():
    assert Square.is_valid_square('e4') == True
    assert Square.is_valid_square('a9') == False
    assert Square.is_valid_square('k2') == False
