# move_validator.py

from .gameboard import Gameboard
from .piece import Piece
from .square import Square


def is_legal_move(start_coords: str, end_coords: str, player_color: str,
                  gameboard: Gameboard) -> bool:
    """Check if moving a piece from one square to another is legal.

    Args:
        start_coords: The coordinates of the square the piece is on before the
          move.
        end_coords: The coordinates of the square the piece is on after the
          move.
        player_color: The color of the player making the move.
        gameboard: The Gameboard object.

    Returns:
        A boolean indicating whether or not the move is legal.
    """

    # Check if the square coordinates are valid
    if (not Square.is_valid_square(start_coords) or not
            Square.is_valid_square(end_coords)):
        return False

    # Check if there's a piece on the starting square, and if it belongs
    # to the player.
    if not _is_allowed_start_square(start_coords, player_color, gameboard):
        return False

    # Check if the user's allowed to occupy the end square.
    if not _is_allowed_end_square(end_coords, player_color, gameboard):
        return False

    piece = gameboard.get_square_piece(start_coords)
    return _is_valid_piece_path(piece, start_coords, end_coords, gameboard)


def _is_allowed_start_square(start_coords: str, player_color: str,
                             gameboard: Gameboard) -> bool:
    start_piece = gameboard.get_square_piece(start_coords)
    return start_piece and start_piece.color == player_color


def _is_allowed_end_square(end_coords: str, player_color: str,
                           gameboard: Gameboard) -> bool:
    end_piece = gameboard.get_square_piece(end_coords)
    return not end_piece or end_piece.color != player_color


def _is_valid_piece_path(piece: Piece, start_coords: str, end_coords: str,
                         gameboard: Gameboard) -> bool:
    """Check if the piece can move along the path specified by the coordinates.

    Args:
        piece: A Piece object for the given piece.
        start_coords: The coordinates of the square the piece is on before the
          move.
        end_coords: The coordinates of the square the piece is on after the 
          move.
        gameboard: The Gameboard object.

    Returns:
        A boolean indicating whether or not the piece can move along the
          specified path.
    """
    if piece.symbol == Piece.PAWN:
        pass

    if piece.symbol == Piece.KNIGHT:
        return _is_valid_knight_path(start_coords, end_coords)

    if piece.symbol == Piece.BISHOP:
        return _is_valid_bishop_path(start_coords, end_coords, gameboard)

    if piece.symbol == Piece.ROOK:
        return _is_valid_rook_path(start_coords, end_coords, gameboard)

    if piece.symbol == Piece.QUEEN:
        return _is_valid_queen_path(start_coords, end_coords, gameboard)

    if piece.symbol == Piece.KING:
        return _is_valid_king_path(start_coords, end_coords)


def _is_valid_knight_path(start_coords: str, end_coords: str) -> bool:
    file_start, rank_start = start_coords
    file_end, rank_end = end_coords

    file_dist = _get_file_dist(file_start, file_end)
    rank_dist = _get_rank_dist(rank_start, rank_end)

    return (
        (file_dist == 1 and rank_dist == 2) or
        (file_dist == 2 and rank_dist == 1)
    )


def _is_valid_bishop_path(start_coords: str, end_coords: str,
                          gameboard: Gameboard) -> bool:
    return (_is_diagonal_move(start_coords, end_coords) and not
            _are_pieces_in_the_way(start_coords, end_coords, gameboard))


def _is_valid_rook_path(start_coords: str, end_coords: str,
                        gameboard: Gameboard) -> bool:
    return (
        (_is_horizontal_move(start_coords, end_coords) or
         _is_vertical_move(start_coords, end_coords)) and not
        _are_pieces_in_the_way(start_coords, end_coords, gameboard))


def _is_valid_queen_path(start_coords: str, end_coords: str,
                         gameboard: Gameboard) -> bool:
    return (
        (_is_horizontal_move(start_coords, end_coords) or
         _is_vertical_move(start_coords, end_coords) or
         _is_diagonal_move(start_coords, end_coords)) and not
        _are_pieces_in_the_way(start_coords, end_coords, gameboard))


def _is_valid_king_path(start_coords: str, end_coords: str) -> bool:
    file_start, rank_start = start_coords
    file_end, rank_end = end_coords

    file_dist = _get_file_dist(file_start, file_end)
    rank_dist = _get_rank_dist(rank_start, rank_end)

    # The king may move one square horizontally, vertically or diagonally
    return (
        (file_dist == 1 and rank_dist == 0) or  # Horizontal movement
        (file_dist == 0 and rank_dist == 1) or  # Vertical movement
        (file_dist == 1 and rank_dist == 1)     # Diagonal movement
    )


def _get_file_dist(file1: str, file2: str) -> int:
    # Use the ASCII character codes of the file letters
    return abs(ord(file1) - ord(file2))


def _get_rank_dist(rank1: str, rank2: str) -> int:
    return abs(int(rank1) - int(rank2))


def _is_horizontal_move(start_coords: str, end_coords: str) -> bool:
    file_start, rank_start = start_coords
    file_end, rank_end = end_coords
    return file_start != file_end and rank_start == rank_end


def _is_vertical_move(start_coords: str, end_coords: str) -> bool:
    file_start, rank_start = start_coords
    file_end, rank_end = end_coords
    return file_start == file_end and rank_start != rank_end


def _is_diagonal_move(start_coords: str, end_coords: str) -> bool:
    file_start, rank_start = start_coords
    file_end, rank_end = end_coords

    file_dist = _get_file_dist(file_start, file_end)
    rank_dist = _get_rank_dist(rank_start, rank_end)
    return file_dist == rank_dist and start_coords != end_coords


def _are_pieces_in_the_way(start_coords: str, end_coords: str,
                           gameboard: Gameboard) -> bool:
    board = gameboard.get_board()

    # Extract the files and ranks
    file_start, rank_start = start_coords
    file_end, rank_end = end_coords

    # Convert the files and ranks to rows and columns in the board array
    col_start = Gameboard.file_to_col(file_start)
    col_end = Gameboard.file_to_col(file_end)

    row_start = Gameboard.rank_to_row(rank_start)
    row_end = Gameboard.rank_to_row(rank_end)

    # Check if there are pieces in the way on the same rank
    if _is_horizontal_move(start_coords, end_coords):
        start, end = sorted((col_start, col_end))
        for col in range(start + 1, end):
            if board[row_start][col]:
                return True

    # Check if there are pieces in the way on the same file
    elif _is_vertical_move(start_coords, end_coords):
        start, end = sorted((row_start, row_end))
        for row in range(start + 1, end):
            if board[row][col_start]:
                return True

    # Check if there are pieces in the way diagonally
    elif _is_diagonal_move(start_coords, end_coords):
        row_step = 1 if row_start < row_end else -1
        col_step = 1 if col_start < col_end else -1

        row, col = row_start + row_step, col_start + col_step
        while col != col_end and row != row_end:
            if board[row][col]:
                return True
            row += row_step
            col += col_step

    return False
