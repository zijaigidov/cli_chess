# gameboard.py

import copy


class Square:
    """A square on the chess board."""

    def __init__(self, piece=None):
        """Initialize the square with a piece."""
        self.piece = piece

    def is_empty(self):
        return self.piece is None


class Gameboard:
    """The chess game board."""

    # The rank numbers and file letters are written from white's perspective
    RANK_NUMBERS = tuple(range(8, 0, -1))
    FILE_LETTERS = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')
    LENGTH = 8

    def __init__(self):
        self.__board = self.__initialize_board()

    def __initialize_board(self):
        """Initialize the game board."""
        '''
        The board is implemented as a 2D list, where the first index relates to
        the rank and the second index relates to the number of the file.
        - board[0][0] corresponds to the top-left square
        - board[7][7] corresponds to the bottom-right square
        '''
        board = [
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ]

        # Convert all of the board squares into Square objects
        for row in range(Gameboard.LENGTH):
            for col in range(Gameboard.LENGTH):
                value = board[row][col]
                board[row][col] = Square(value) if value else Square()

    def get_board(self):
        """Get a copy of the game board."""
        return copy.deepcopy(self.__board)
