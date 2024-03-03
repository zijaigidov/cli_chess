# square.py

from .board_info import BoardInfo


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


class Square:
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
