from typing import List


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
            for element in self.board:
                if element is None:
                    return False
        return True

    def valid(self, position: int) -> bool:
        coordinate = keypad_to_coordinate(position)
        return self.board[coordinate[0]][coordinate[1]] is None


def keypad_to_coordinate(position: int) -> tuple:
    if position == 7:
        return 0, 0
    elif position == 8:
        return 0, 1
    elif position == 9:
        return 0, 2
    elif position == 4:
        return 1, 0
    elif position == 5:
        return 1, 1
    elif position == 6:
        return 1, 2
    elif position == 1:
        return 2, 0
    elif position == 2:
        return 2, 1
    elif position == 3:
        return 2, 2
    else:
        raise ValueError
