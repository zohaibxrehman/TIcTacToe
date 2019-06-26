from typing import List, Optional
import random


class Board:
    """
    A 3x3 board for playing Tic-Tac-Toe

    === Attributes ===
    board: contains the elements of our board

    === Representation Invariants ===
    - This board list consists of three lists.
    - Each of these three lists have three elements.
    - These elements are either the string 'X' or 'O' or NoneType.

    """
    board: List[List[str]]

    def __init__(self) -> None:
        """Initialises the board.
        """
        self.board = [[None, None, None],
                      [None, None, None],
                      [None, None, None]]

    def __getitem__(self, key: int) -> str:
        """Return item at the board's <key> keypad position.

        Precondition: 1 <= key <= 9
        """
        coordinate = keypad_to_coordinate(key)
        return self.board[coordinate[0]][coordinate[1]]

    def move(self, position, char: str) -> None:
        """Insert <char> at board's keypad position <position>.

        Precondition: char == 'X' or char == 'O'
        """
        coordinate = keypad_to_coordinate(position)
        if self.board[coordinate[0]][coordinate[1]] is None:
            self.board[coordinate[0]][coordinate[1]] = char

    def is_straight(self) -> bool:
        """Return True if there is a three-in-a-row else False.
        """
        for i in range(3):
            if self.board[i][0] is not None and \
                    self.board[i][0] == self.board[i][1] == self.board[i][2]:
                return True

            if self.board[0][i] is not None and \
                    self.board[0][i] == self.board[1][i] == self.board[2][i]:
                return True

        if self.board[0][0] is not None and \
                self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return True

        if self.board[0][2] is not None and \
                self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return True

        return False

    def is_full(self) -> bool:
        """Return True if board is full else False.
        """
        for row in self.board:
            for element in row:
                if element is None:
                    return False
        return True

    def is_empty(self) -> bool:
        """
        Return True if board is empty else False.
        """

        for row in self.board:
            for element in row:
                if element is not None:
                    return False
        return True

    def valid_inputs(self) -> list:
        """Return a list of all keypad inputs that can be played on the board.
        """

        valid_inputs = []
        for x in range(3):
            for y in range(3):
                if self.board[x][y] is None:
                    valid_inputs.append(coordinate_to_keypad((x, y)))
        return valid_inputs

    def empty_corner(self) -> Optional[int]:
        """Return a random corner keypad position which is of NoneType(empty).
        """
        # randomness added to add an illusion of intelligence. otherwise will
        # always play same and look mechanical
        empty_corners = []
        if self.board[0][0] is None:
            empty_corners.append(7)
        if self.board[0][2] is None:
            empty_corners.append(9)
        if self.board[2][0] is None:
            empty_corners.append(1)
        if self.board[2][2] is None:
            empty_corners.append(3)

        if len(empty_corners) != 0:
            return random.choice(empty_corners)
        else:
            return None

    def empty_side(self) -> Optional[int]:
        """Return a random centre edge keypad position which is of
        NoneType(empty).
        """
        empty_corners = []
        if self.board[0][1] is None:
            empty_corners.append(8)
        if self.board[1][0] is None:
            empty_corners.append(4)
        if self.board[1][2] is None:
            empty_corners.append(6)
        if self.board[2][1] is None:
            empty_corners.append(2)

        if len(empty_corners) != 0:
            return random.choice(empty_corners)
        else:
            return None


KEYPAD_TO_COORDINATE = {7: (0, 0), 8: (0, 1), 9: (0, 2),
                        4: (1, 0), 5: (1, 1), 6: (1, 2),
                        1: (2, 0), 2: (2, 1), 3: (2, 2)}
COORDINATE_TO_KEYPAD = {c: k for k, c in KEYPAD_TO_COORDINATE.items()}


def keypad_to_coordinate(key: int) -> tuple:
    """Return a tuple which contains the indices of <key> keypad position.
    """
    if key in KEYPAD_TO_COORDINATE:
        return KEYPAD_TO_COORDINATE[key]
    else:
        raise ValueError


def coordinate_to_keypad(coordinate: tuple) -> int:
    """Return a tuple which contains the keypad position of <coordinate> board
    indices.
    """
    if coordinate in COORDINATE_TO_KEYPAD:
        return COORDINATE_TO_KEYPAD[coordinate]
    else:
        raise ValueError
