from typing import List

class Board:
    """


    === Representation Invariants ===
    - attribute board is list. This list consists of three lists. Each
    of these three lists have three elements. These elements are either the
    string 'X' or 'O' or NoneType.
    """
    board: List[List[str]]

    def __init__(self):
        """

        """
        board = [[None, None, None],[None, None, None],[None, None, None]]

    def move(self):
        """

        :return:
        """

    def is_winning(self):
        """

        :return:
        """

