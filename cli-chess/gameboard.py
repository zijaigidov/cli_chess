# gameboard.py

import copy

import gamepieces


class Square:
    def __init__(self, piece=None):
        self.piece = piece

    def is_empty(self):
        return self.piece is None


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
                self._add_board_piece(row, col, piece_symbol, 'black')

        # Add the white pieces
        WHITE_RANGE = range(Gameboard.LENGTH - len(INITIAL_PIECES),
                            Gameboard.LENGTH)
        for row in WHITE_RANGE:
            for col in range(Gameboard.LENGTH):
                piece_symbol = INITIAL_PIECES[Gameboard.LENGTH - 1 - row][col]
                self._add_board_piece(row, col, piece_symbol, 'white')

    def _initialize_board(self) -> None:
        """Initialize the state of the game board."""
        self._initialize_empty_board()
        self._add_initial_pieces()

    def get_board_copy(self):
        return copy.deepcopy(self._board)
