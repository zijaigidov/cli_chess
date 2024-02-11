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
    LENGTH = 8

    # The rank numbers and file letters are written from white's perspective
    RANK_NUMBERS = tuple(range(8, 0, -1))
    FILE_LETTERS = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')

    '''
    The board is implemented as a 2D list, where the first index relates to the
    rank and the second index relates to the number of the file.
    - board[0][0] corresponds to the top-left square
    - board[7][7] corresponds to the bottom-right square
    '''
    INITIAL_BOARD = [
        ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
        ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
    ]

    def __init__(self):
        """Initialize the game board."""
        self.__board = Gameboard.INITIAL_BOARD

    def get_board(self):
        """Get a copy of the game board."""
        return copy.deepcopy(self.__board)

    def print_board(self, color):
        """
        Print the board from the perspective of the player with the given color.
        """
        if color == 'white':
            for i in range(Gameboard.LENGTH):
                rank_number = Gameboard.RANK_NUMBERS[i]
                rank = ' '.join(self.__board[i])
                print(f'{rank_number}   {rank}')
            print(f'\n    {" ".join(Gameboard.FILE_LETTERS)}')

        elif color == 'black':
            for i in reversed(range(Gameboard.LENGTH)):
                rank_number = Gameboard.RANK_NUMBERS[i]
                rank = ' '.join(reversed(self.__board[i]))
                print(f'{rank_number}   {rank}')
            print(f'\n    {" ".join(reversed(Gameboard.FILE_LETTERS))}')
