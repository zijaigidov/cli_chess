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
        self._board = self._initialize_board()

    def _initialize_board(self):
        '''
        The board is implemented as a 2D list, where the first index relates to
        the rank and the second index relates to the number of the file.
        - board[0][0] corresponds to the top-left square
        - board[7][7] corresponds to the bottom-right square
        '''
        board = [
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ]

        # Convert all of the board squares into Square objects
        for row in range(Gameboard.LENGTH):
            for col in range(Gameboard.LENGTH):
                val = board[row][col]
                if val in gamepieces.PIECES:
                    board[row][col] = Square(val)
                else:
                    board[row][col] = Square()

    def get_board_copy(self):
        return copy.deepcopy(self._board)
