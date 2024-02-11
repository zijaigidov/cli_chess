# main.py

import copy


class Player:
    """A player."""

    def __init__(self, color):
        """Initializes the player object with a color."""
        self.color = color


class Gameboard:
    """The chess game board."""

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
            for rank in self.__board:
                print(' '.join(rank))

        elif color == 'black':
            for rank in reversed(self.__board):
                print(' '.join(reversed(rank)))


def main():
    pass


if __name__ == '__main__':
    main()
