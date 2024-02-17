# movevalidator.py

from gameboard import Gameboard


class MoveValidator:
    """Chess move validator."""

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
        return file in Gameboard.FILE_LETTERS and rank in Gameboard.RANK_NUMBERS
