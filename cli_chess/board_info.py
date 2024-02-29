# board_info.py

from dataclasses import dataclass


@dataclass
class BoardInfo:
    """Information about the chess board."""
    # NOTE: The files and ranks are ordered from the white player's perspective.
    FILE_LETTERS = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')
    RANK_NUMBERS = (8, 7, 6, 5, 4, 3, 2, 1)
    LENGTH = 8
