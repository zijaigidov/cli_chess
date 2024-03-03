# move_validator.py

from .gameboard import Gameboard
from .piece import Piece
from .square import Square


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

    @staticmethod
    def _is_valid_piece_path(piece: Piece,
                             start_coordinates: str,
                             end_coordinates: str,
                             gameboard: Gameboard) -> bool:
        """Check if the piece can move along the path specified by the
        coordinates.

        Args:
            piece: A Piece object for the given piece.
            start_coordinates: The coordinates of the square the piece is on
              before the move.
            end_coordinates: The coordinates of the square the piece is on
              after the move.
            gameboard: The Gameboard object.

        Returns:
            A boolean indicating whether or not the piece can move along the
              specified path.
        """
        if piece.symbol == Piece.PAWN:
            pass
        if piece.symbol == Piece.KNIGHT:
            return MoveValidator._is_valid_knight_path(
                start_coordinates, end_coordinates)
        if piece.symbol == Piece.BISHOP:
            return MoveValidator._is_valid_bishop_path(
                start_coordinates, end_coordinates, gameboard)
        if piece.symbol == Piece.ROOK:
            return MoveValidator._is_valid_rook_path(
                start_coordinates, end_coordinates, gameboard)
        if piece.symbol == Piece.QUEEN:
            return MoveValidator._is_valid_queen_path(
                start_coordinates, end_coordinates, gameboard)
        if piece.symbol == Piece.KING:
            return MoveValidator._is_valid_king_path(
                start_coordinates, end_coordinates)

    @staticmethod
    def _is_valid_knight_path(start_coordinates: str,
                              end_coordinates: str) -> bool:
        file_start, rank_start = start_coordinates
        file_end, rank_end = end_coordinates

        file_dist = MoveValidator._get_file_distance(file_start, file_end)
        rank_dist = MoveValidator._get_rank_distance(rank_start, rank_end)

        return (
            (file_dist == 1 and rank_dist == 2) or
            (file_dist == 2 and rank_dist == 1)
        )

    @staticmethod
    def _is_valid_bishop_path(start_coordinates: str,
                              end_coordinates: str,
                              gameboard: Gameboard) -> bool:
        return (
            MoveValidator._is_diagonal_move(
                start_coordinates, end_coordinates, gameboard) and not
            MoveValidator._are_pieces_in_the_way(
                start_coordinates, end_coordinates, gameboard)
        )

    @staticmethod
    def _is_valid_rook_path(start_coordinates: str,
                            end_coordinates: str,
                            gameboard: Gameboard) -> bool:
        return (
            MoveValidator._is_horizontal_move(
                start_coordinates, end_coordinates, gameboard) and not
            MoveValidator._are_pieces_in_the_way(
                start_coordinates, end_coordinates, gameboard)
        )

    @staticmethod
    def _is_valid_queen_path(start_coordinates: str,
                             end_coordinates: str,
                             gameboard: Gameboard) -> bool:
        return (
            (MoveValidator._is_horizontal_move(
                start_coordinates, end_coordinates, gameboard) or
             MoveValidator._is_vertical_move(
                start_coordinates, end_coordinates, gameboard) or
             MoveValidator._is_diagonal_move(
                start_coordinates, end_coordinates, gameboard)) and not
            MoveValidator._are_pieces_in_the_way(
                start_coordinates, end_coordinates, gameboard)
        )

    @staticmethod
    def _is_valid_king_path(start_coordinates: str,
                            end_coordinates: str) -> bool:
        file_start, rank_start = start_coordinates
        file_end, rank_end = end_coordinates

        file_dist = MoveValidator._get_file_distance(file_start, file_end)
        rank_dist = MoveValidator._get_rank_distance(rank_start, rank_end)

        # The king may move one square horizontally, vertically or diagonally
        return (
            (file_dist == 1 and rank_dist == 0) or  # Horizontal movement
            (file_dist == 0 and rank_dist == 1) or  # Vertical movement
            (file_dist == 1 and rank_dist == 1)     # Diagonal movement
        )

    @staticmethod
    def _get_file_distance(file1: str, file2: str) -> int:
        # Use the ASCII character codes of the file letters
        return abs(ord(file1) - ord(file2))

    @staticmethod
    def _get_rank_distance(rank1: str, rank2: str) -> int:
        return abs(int(rank1) - int(rank2))

    @staticmethod
    def _is_horizontal_move(start_coordinates: str,
                            end_coordinates: str) -> bool:
        file_start, rank_start = start_coordinates
        file_end, rank_end = end_coordinates
        return file_start != file_end and rank_start == rank_end

    @staticmethod
    def _is_vertical_move(start_coordinates: str,
                          end_coordinates: str) -> bool:
        file_start, rank_start = start_coordinates
        file_end, rank_end = end_coordinates
        return file_start == file_end and rank_start != rank_end

    @staticmethod
    def _is_diagonal_move(start_coordinates: str,
                          end_coordinates: str) -> bool:
        file_start, rank_start = start_coordinates
        file_end, rank_end = end_coordinates

        file_dist = MoveValidator._get_file_distance(file_start, file_end)
        rank_dist = MoveValidator._get_rank_distance(rank_start, rank_end)
        return file_dist == rank_dist and start_coordinates != end_coordinates

    @staticmethod
    def _are_pieces_in_the_way(start_coordinates: str,
                               end_coordinates: str,
                               gameboard: Gameboard) -> bool:
        board = gameboard.get_board()

        # Extract the files and ranks
        file_start, rank_start = start_coordinates
        file_end, rank_end = end_coordinates

        # Convert the files and ranks to rows and columns in the board array
        col_start = Gameboard.file_to_col(file_start)
        col_end = Gameboard.file_to_col(file_end)

        row_start = Gameboard.rank_to_row(rank_start)
        row_end = Gameboard.rank_to_row(rank_end)

        # Check if there are pieces in the way on the same rank
        if MoveValidator._is_horizontal_move(
                start_coordinates, end_coordinates):
            start, end = sorted((col_start, col_end))
            for col in range(start + 1, end):
                if board[row_start][col]:
                    return True

        # Check if there are pieces in the way on the same file
        elif MoveValidator._is_vertical_move(
                start_coordinates, end_coordinates):
            start, end = sorted((row_start, row_end))
            for row in range(start + 1, end):
                if board[row][col_start]:
                    return True

        # Check if there are pieces in the way diagonally
        elif MoveValidator._is_diagonal_move(
                start_coordinates, end_coordinates):
            row_step = 1 if row_start < row_end else -1
            col_step = 1 if col_start < col_end else -1

            row, col = row_start + row_step, col_start + col_step
            while col != col_end and row != row_end:
                if board[row][col]:
                    return True
                row += row_step
                col += col_step

        return False
