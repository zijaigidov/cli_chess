# move_validator.py

from .square import Square
from .gameboard import Gameboard


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
            end_coordinates: The coordinates of the square the piece is on after the
              move.
            player_color: The color of the player making the move.
            gameboard: The Gameboard object.

        Returns:
            A boolean indicating whether or not the move is legal.
        """

        # Check if the square coordinates are valid
        if (not Square.is_valid_square(start_coordinates) or
                not Square.is_valid_square(end_coordinates)):
            return False

        # Check if there's a piece on the starting square, and if it belongs
        # to the player.
        if not MoveValidator._is_allowed_start_square(
                start_coordinates, player_color, gameboard):
            return False

        # Check if the user's allowed to occupy the end square.
        if not MoveValidator._is_allowed_end_square(
                end_coordinates, player_color, gameboard):
            return False

    @staticmethod
    def _is_allowed_start_square(start_coordinates: str,
                                 player_color: str,
                                 gameboard: Gameboard) -> bool:
        start_piece = gameboard.get_square_piece(start_coordinates)
        return start_piece and start_piece.color == player_color

    @staticmethod
    def _is_allowed_end_square(end_coordinates: str,
                               player_color: str,
                               gameboard: Gameboard) -> bool:
        end_piece = gameboard.get_square_piece(end_coordinates)
        return not end_piece or end_piece.color != player_color
