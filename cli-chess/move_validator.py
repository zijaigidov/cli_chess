# move_validator.py

from error import InvalidSquareError
from square import Square


class MoveValidator:
    """Chess move validator."""

    @staticmethod
    def is_legal_move(start_coordinates: str,
                      end_coordinates: str,
                      player_color: str,
                      board) -> bool:
        """Check if moving a piece from one square to another is legal.

        Args:
            start_coordinates: The coordinates of the square the piece is on
              before the move.
            end_square: The coordinates of the square the piece is on after the
              move.
            player_color: The color of the player making the move.
            board: The chess board.

        Returns:
            A boolean indicating whether or not the move is legal.

        Raises:
            InvalidSquareError: If invalid square coordinates are passed.
        """

        # Check if the square coordinates are valid
        if not Square.is_valid_square(start_coordinates):
            raise InvalidSquareError(f"invalid square: '{start_coordinates}'")
        elif not Square.is_valid_square(end_coordinates):
            raise InvalidSquareError(f"invalid square: '{end_coordinates}'")
