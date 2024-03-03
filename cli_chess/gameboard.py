# gameboard.py


import copy
from dataclasses import dataclass
from typing import List

from .board_info import BoardInfo
from .error import InvalidSquareError
from .square import Square, Piece


@dataclass
class Color:
    """A chess player's color."""
    WHITE: str = 'white'
    BLACK: str = 'black'


class Gameboard:
    # Note: whitespace strings have been added for formatting purposes
    INITIAL_BOARD_STATE = [
        ['R_b', 'N_b', 'B_b', 'Q_b', 'K_b', 'B_b', 'N_b', 'R_b'],
        ['P_b', 'P_b', 'P_b', 'P_b', 'P_b', 'P_b', 'P_b', 'P_b'],
        ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
        ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
        ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
        ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
        ['P_w', 'P_w', 'P_w', 'P_w', 'P_w', 'P_w', 'P_w', 'P_w'],
        ['R_w', 'N_w', 'B_w', 'Q_w', 'K_w', 'B_w', 'N_w', 'R_w']
    ]

    def __init__(self,
                 board_state: List[List[str]] = INITIAL_BOARD_STATE) -> None:
        """Initialize the chess board with an optional board state.

        If no board state is given, the board is initialized as the starting 
        board.

        Args:
            board_state: A 2D list representation of the board with strings to
              denote the pieces. The strings consist of a piece symbol, a
              separator, and a color, e.g. 'K_w' for the white king. If a board 
              square is empty, the corresponding string is denoted by three 
              whitespace characters.
        """
        self._board = Gameboard._initialize_board(board_state)

    def _initialize_board(
            board_state: List[List[str]]) -> List[List[Piece | None]]:
        """Return the initialized board.

        Returns:
            A 2D list representation of the board which contains Piece objects
            or None where there are none.
        """
        def piece_repr_to_piece(piece_repr: str) -> Piece | None:
            piece_symbol = Piece.extract_symbol_from_repr(piece_repr)
            if piece_symbol in Piece.PIECES:
                return Piece(piece_repr)
            return None

        initialized_board = []
        for row in board_state:
            initialized_row = []
            for piece in row:
                initialized_row.append(piece_repr_to_piece(piece))
            initialized_board.append(initialized_row)

        return initialized_board

    def play_move(self,
                  start_coordinates: str,
                  end_coordinates: str) -> None:
        """Move a piece from one square to another.

        Args:
            start_coordinates: The coordinates of the square the piece is on
              before the move.
            end_coordinates: The coordinates of the square the piece is on after
              the move.
        """
        # Extract the files and ranks
        file_start, rank_start = start_coordinates
        file_end, rank_end = end_coordinates

        # Get the corresponding rows and columns
        row_start = Gameboard.rank_to_row(rank_start)
        row_end = Gameboard.rank_to_row(rank_end)

        col_start = Gameboard.file_to_col(file_start)
        col_end = Gameboard.file_to_col(file_end)

        # Move the piece from the starting square to the end square
        self._board[row_end][col_end] = self._board[row_start][col_start]
        self._board[row_start][col_start] = None

    def print_board(self) -> None:
        """Print the chess board as seen by the white player, with the ranks and
        files shown."""
        board_len = len(self._board)

        for row in range(board_len):
            print(BoardInfo.RANK_NUMBERS[row], end='   ')
            for col in range(board_len):
                piece = self._board[row][col]
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
        col = Gameboard.file_to_col(file)
        row = Gameboard.rank_to_row(rank)

        return copy.copy(self._board[row][col])

    @staticmethod
    def file_to_col(file: str) -> int:
        """Map a chess file (a-h) to the corresponding board column (0-7)."""
        # Since the files (a-h) map to the column indices (0-7) in ascending
        # order, the relative order of the file characters can be used to get
        # the corresponding column index.
        return ord(file) - ord('a')

    @staticmethod
    def rank_to_row(rank: str) -> int:
        """Map a chess rank (1-8) to the corresponding board row (7-0)."""
        # This makes use of the fact that the rank number (1-8) and the
        # corresponding row index (7-0) always add up to the board length (8).
        return BoardInfo.LENGTH - int(rank)
