# gameboard.py

import copy
from dataclasses import dataclass
from typing import Optional

import gamepieces


class Piece:
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


@dataclass
class Color:
    """A chess player's color."""
    WHITE: str = 'white'
    BLACK: str = 'black'


@dataclass
class BoardInfo:
    """Information about the chess board."""
    # NOTE: The files and ranks are ordered from the white player's perspective.
    FILE_LETTERS = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')
    RANK_NUMBERS = (8, 7, 6, 5, 4, 3, 2, 1)
    LENGTH = 8


class Gameboard:
    def __init__(self):
        self._initialize_board()

    def _initialize_empty_board(self) -> None:
        """Initialize an empty board."""
        self._board = [[Square() for _ in range(BoardInfo.LENGTH)]
                       for _ in range(BoardInfo.LENGTH)]

    def _add_board_piece(self, row: int, col: int, symbol: str,
                         color: str) -> None:
        """Add a piece to the board on the specified position."""
        square = self._board[row][col]
        square.piece = Piece(symbol, color)

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
                square = self._board[i][j]
                if not square.is_empty():
                    print(square.piece.symbol, end=' ')
                else:
                    print(' ', end=' ')
            print()
        print(f'\n    {" ".join(BoardInfo.FILE_LETTERS)}')
