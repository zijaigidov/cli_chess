# gameboard.py

import copy
from dataclasses import dataclass

import gamepieces


class Square:
    def __init__(self, piece=None):
        self.piece = piece

    def is_empty(self):
        return self.piece is None


@dataclass
class Color:
    """A chess player's color."""
    WHITE: str = 'white'
    BLACK: str = 'black'


class Piece:
    def __init__(self, piece_symbol, color):
        self.piece = piece_symbol
        self.color = color


class Gameboard:
    LENGTH = 8

    def __init__(self):
        self._initialize_board()

    def _initialize_empty_board(self) -> None:
        """Initialize an empty board."""
        self._board = [[Square() for _ in range(Gameboard.LENGTH)]
                       for _ in range(Gameboard.LENGTH)]

    def _add_board_piece(self, row: int, col: int, piece_symbol: str,
                         color: str) -> None:
        """Add a piece to the board on the specified position."""
        square = self._board[row][col]
        square.piece = Piece(piece_symbol, color)

    def _add_initial_pieces(self) -> None:
        """Add the initial pieces to the board."""
        INITIAL_PIECES = (
            ('R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'),
            ('P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'),
        )

        # Add the black pieces
        BLACK_RANGE = range(len(INITIAL_PIECES))
        for row in BLACK_RANGE:
            for col in range(Gameboard.LENGTH):
                piece_symbol = INITIAL_PIECES[row][col]
                self._add_board_piece(row, col, piece_symbol, Color.BLACK)

        # Add the white pieces
        WHITE_RANGE = range(Gameboard.LENGTH - len(INITIAL_PIECES),
                            Gameboard.LENGTH)
        for row in WHITE_RANGE:
            for col in range(Gameboard.LENGTH):
                piece_symbol = INITIAL_PIECES[Gameboard.LENGTH - 1 - row][col]
                self._add_board_piece(row, col, piece_symbol, Color.WHITE)

    def _initialize_board(self) -> None:
        """Initialize the state of the game board."""
        self._initialize_empty_board()
        self._add_initial_pieces()

    def print_board(self) -> None:
        """Print the chess board as seen by the white player, with rank numbers
        and file letters."""
        RANK_NUMBERS = (8, 7, 6, 5, 4, 3, 2, 1)
        FILE_LETTERS = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')

        for i in range(Gameboard.LENGTH):
            print(RANK_NUMBERS[i], end='   ')
            for j in range(Gameboard.LENGTH):
                square = self._board[i][j]
                if not square.is_empty():
                    print(square.piece.piece, end=' ')
                else:
                    print(' ', end=' ')
            print()
        print(f'\n    {" ".join(FILE_LETTERS)}')

    def get_board_copy(self):
        return copy.deepcopy(self._board)