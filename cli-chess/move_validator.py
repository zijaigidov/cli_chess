# move_validator.py

from gameboard import Square


class InvalidSquareError (Exception):
    pass


class MoveValidator:
    """Chess move validator."""

    @staticmethod
    def is_legal_move(start_square: str,
                      end_square: str,
                      player_color: str,
                      board) -> bool:
        """Check if moving a piece from one square to another is legal.

        Args:
            start_square: A string representing the square of the piece prior
              to the move.
            end_square: A string representing the square of the piece after the
              move.
            player_color: A string representing the color of the player making
              the move.
            board: The chess board.

        Returns:
            A boolean indicating whether or not the move is legal.

        Raises:
            InvalidSquareError: If an invalid square is passed.
        """

        # Check if the squares are valid
        if not Square.is_valid_square(start_square):
            raise InvalidSquareError(f"invalid square: '{start_square}'")
        elif not Square.is_valid_square(end_square):
            raise InvalidSquareError(f"invalid square: '{end_square}'")
