# gameboard.py


import copy
from dataclasses import dataclass

from board_info import BoardInfo
from error import InvalidSquareError
from square import Square, Piece


@dataclass
class Color:
    """A chess player's color."""
    WHITE: str = 'white'
    BLACK: str = 'black'


class Gameboard:
    def __init__(self):
        self._initialize_board()

    def _initialize_empty_board(self) -> None:
        """Initialize an empty board."""
        self._board = [
            [None] * BoardInfo.LENGTH for _ in range(BoardInfo.LENGTH)]

    def _add_board_piece(self, row: int, col: int, symbol: str,
                         color: str) -> None:
        """Add a piece to the board on the specified position."""
        self._board[row][col] = Piece(symbol, color)

    def _add_initial_pieces(self) -> None:
        """Add the initial pieces to the board."""
        INITIAL_PIECES = (
            ('R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'),
            ('P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'),
        )

        # Add the black pieces
        BLACK_RANGE = range(len(INITIAL_PIECES))
        for row in BLACK_RANGE:
            for col in range(BoardInfo.LENGTH):
                piece_symbol = INITIAL_PIECES[row][col]
                self._add_board_piece(row, col, piece_symbol, Color.BLACK)

        # Add the white pieces
        WHITE_RANGE = range(BoardInfo.LENGTH - len(INITIAL_PIECES),
                            BoardInfo.LENGTH)
        for row in WHITE_RANGE:
            for col in range(BoardInfo.LENGTH):
                piece_symbol = INITIAL_PIECES[BoardInfo.LENGTH - 1 - row][col]
                self._add_board_piece(row, col, piece_symbol, Color.WHITE)

    def _initialize_board(self) -> None:
        """Initialize the state of the game board."""
        self._initialize_empty_board()
        self._add_initial_pieces()

    def print_board(self) -> None:
        """Print the chess board as seen by the white player, with rank numbers
        and file letters."""
        for i in range(BoardInfo.LENGTH):
            print(BoardInfo.RANK_NUMBERS[i], end='   ')
            for j in range(BoardInfo.LENGTH):
                piece = self._board[i][j]
                if piece:
                    print(piece.symbol, end=' ')
                else:
                    print(' ', end=' ')
            print()
        print(f'\n    {" ".join(BoardInfo.FILE_LETTERS)}')

    def get_board(self) -> list[list[Square]]:
        """Get a copy of the game board.

        Returns:
            A copy of the 2D-array used to store the board state.
        """
        return copy.deepcopy(self._board)

    def get_square_piece(self, square_coordinates: str) -> Piece | None:
        """Get a copy of the piece on the square with the given coordinates.

        Args:
            square_coordinates: The coordinates of the square, where the first 
              character is the fileand the second is the rank, e.g. 'e4'.

        Returns:
            A copy of the Piece object on the square, or None if there is none.

        Raises:
            InvalidSquareError: If the coordinates for the square are invalid.
        """
        if not Square.is_valid_square(square_coordinates):
            raise InvalidSquareError(f"invalid square: '{square_coordinates}'")

        file, rank = square_coordinates
        col = Gameboard._file_to_col(file)
        row = Gameboard._rank_to_row(rank)

        return copy.copy(self._board[row][col])

    @staticmethod
    def _file_to_col(file: str) -> int:
        """Map a chess file (a-h) to the corresponding board column (0-7)."""
        # Since the files (a-h) map to the column indices (0-7) in ascending
        # order, the relative order of the file characters can be used to get
        # the corresponding column index.
        return ord(file) - ord('a')

    @staticmethod
    def _rank_to_row(rank: str) -> int:
        """Map a chess rank (1-8) to the corresponding board row (7-0)."""
        # This makes use of the fact that the rank number (1-8) and the
        # corresponding row index (7-0) always add up to the board length (8).
        return BoardInfo.LENGTH - int(rank)
