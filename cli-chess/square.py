# square.py

from typing import Optional

from gameboard import BoardInfo


class Piece:
    KING = 'K'
    QUEEN = 'Q'
    ROOK = 'R'
    BISHOP = 'B'
    KNIGHT = 'N'
    PAWN = 'P'
    PIECES = {KING, QUEEN, ROOK, BISHOP, KNIGHT, PAWN}

    def __init__(self, symbol: str, color: str):
        self.symbol = symbol
        self.color = color


class Square:
    def __init__(self, piece: Optional[Piece] = None):
        self.piece = piece

    def is_empty(self) -> bool:
        return self.piece is None

    @staticmethod
    def is_valid_square(square_coordinates: str) -> bool:
        """Check if a square described by a file and rank is valid.

        Args:
            square_coordinates: A string where the first character is the file
              letter and and the second is the rank number, e.g. 'E4'.

        Returns:
            A boolean indicating whether or not the square is a valid square.
        """
        if len(square_coordinates) != 2:
            return False

        file = square_coordinates[0].upper()
        rank = int(square_coordinates[1])
        return file in BoardInfo.FILE_LETTERS and rank in BoardInfo.RANK_NUMBERS
