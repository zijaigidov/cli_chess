# move_validator.py

from square import Square
from gameboard import Gameboard


class MoveValidator:
    """Chess move validator."""

    @staticmethod
    def is_legal_move(start_coordinates: str,
                      end_coordinates: str,
                      player_color: str,
                      gameboard: Gameboard) -> bool:
        """Check if moving a piece from one square to another is legal.

        Args:
            start_coordinates: The coordinates of the square the piece is on
              before the move.
            end_square: The coordinates of the square the piece is on after the
              move.
            player_color: The color of the player making the move.
            gameboard: The Gameboard object.

        Returns:
            A boolean indicating whether or not the move is legal.
        """

        # Check if the square coordinates are valid
        start_valid = Square.is_valid_square(start_coordinates)
        end_valid = Square.is_valid_square(end_coordinates)
        if not start_valid or not end_valid:
            return False

        # Check if there's a piece on the starting square and if it belongs to
        # the player making the move.
        start_piece = gameboard.get_square_piece(start_coordinates)
        if not start_piece or not start_piece.color == player_color:
            return False

        # Check that the end square doesn't have a piece of the same color
        end_piece = gameboard.get_square_piece(end_coordinates)
        if end_piece and end_piece.color == player_color:
            return False
