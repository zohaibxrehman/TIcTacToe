from typing import List

# generator expr


class Board:
    """


    === Representation Invariants ===
    - attribute board is list. This list consists of three lists. Each
    of these three lists have three elements. These elements are either the
    string 'X' or 'O' or NoneType.
    """
    board: List[List[str]]

    def __init__(self) -> None:
        """

        """
        self.board = [[None, None, None],
                      [None, None, None],
                      [None, None, None]]

    def move(self, position, char: str):
        coordinate = keypad_to_coordinate(position)
        if self.board[coordinate[0]][coordinate[1]] is None:
            self.board[coordinate[0]][coordinate[1]] = char

    def is_straight(self) -> bool:
        """

        :return:
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
        for row in self.board:
            for element in row:
                if element is None:
                    return False
        return True

    def is_valid(self, position: int) -> bool:
        coordinate = keypad_to_coordinate(position)
        return self.board[coordinate[0]][coordinate[1]] is None

    def valid_inputs(self) -> list:
        valid_inputs = []
        for x in range(3):
            for y in range(3):
                if self.board[x][y] is None:
                    valid_inputs.append(coordinate_to_keypad((x, y)))
        return valid_inputs


KEYPAD_TO_COORDINATE = {7: (0, 0), 8: (0, 1), 9: (0, 2),
                        4: (1, 0), 5: (1, 1), 6: (1, 2),
                        1: (2, 0), 2: (2, 1), 3: (2, 2)}
COORDINATE_TO_KEYPAD = {c: k for k, c in KEYPAD_TO_COORDINATE.items()}


def keypad_to_coordinate(position: int) -> tuple:
    print(position)
    if position in KEYPAD_TO_COORDINATE:
        return KEYPAD_TO_COORDINATE[position]
    else:
        raise ValueError


def coordinate_to_keypad(coordinate: tuple) -> tuple:
    if coordinate in COORDINATE_TO_KEYPAD:
        return COORDINATE_TO_KEYPAD[coordinate]
    else:
        raise ValueError
