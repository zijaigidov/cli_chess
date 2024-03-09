# square.py

from .board_info import BoardInfo


class Square:
    @staticmethod
    def is_valid_square(square_coords: str) -> bool:
        """Check if a square described by a file and rank is valid.

        Args:
            square_coords: A string where the first character is the file letter
              and and the second is the rank number, e.g. 'E4'.

        Returns:
            A boolean indicating whether or not the square is a valid square.
        """
        if len(square_coords) != 2:
            return False

        file = square_coords[0].upper()
        rank = int(square_coords[1])
        return file in BoardInfo.FILE_LETTERS and rank in BoardInfo.RANK_NUMBERS
