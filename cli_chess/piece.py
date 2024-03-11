# piece.py

from dataclasses import dataclass


@dataclass
class Color:
    """A chess player's color."""
    WHITE: str = 'white'
    BLACK: str = 'black'


class Piece:
    KING = 'K'
    QUEEN = 'Q'
    ROOK = 'R'
    BISHOP = 'B'
    KNIGHT = 'N'
    PAWN = 'P'
    PIECES = {KING, QUEEN, ROOK, BISHOP, KNIGHT, PAWN}

    def __init__(self, piece_repr: str) -> None:
        """Initialize a Piece object from the string representation of a piece.

        Args:
            piece_repr: A representation of a chess piece that consists of a
              character for the piece, an underscore separator, and a character
              for the color, e.g. 'K_w' for the white king.
        """
        self.symbol = Piece.extract_symbol_from_repr(piece_repr)
        self.color = Piece.extract_color_from_repr(piece_repr)

    @staticmethod
    def extract_symbol_from_repr(piece_repr: str) -> str:
        """Extract the piece symbol from the string representation of a piece.

        Args:
            piece_repr: A representation of a chess piece that consists of a
              character for the piece, an underscore separator, and a character
              for the color, e.g. 'K_w' for the white king.

        Example:
            extract_symbol_from_piece('K_w') = 'K'
        """
        return piece_repr[0]

    @staticmethod
    def extract_color_from_repr(piece_repr: str) -> str:
        """Extract the piece color from a string representation of a piece.

        Args:
            piece_repr: A representation of a chess piece that consists of a
              character for the piece, an underscore separator, and a character
              for the color, e.g. 'K_w' for the white king.

        Example:
            extract_symbol_from_piece('K_w') = 'w'
        """
        return piece_repr[2]
