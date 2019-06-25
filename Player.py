import Board
import random
from typing import Optional
import copy


class Player:
    """

    """
    name: str
    char: str
    wins: int

    def __init__(self, name: str, char: str) -> None:
        """Initialises the player.
        """
        self.name = name
        self.char = char
        self.wins = 0

    def move(self, board: Board) -> int:
        raise NotImplementedError


class UserPlayer(Player):
    def move(self, board: Board) -> int:
        valid = False
        while not valid:
            position = input(f'{self.name} make a move!')
            position = int(position)
            if position not in board.valid_inputs():
                print('Invalid input. Choose another position...\n')
            else:
                valid = True
        print('')
        return position


class RandomPlayer(Player):
    def move(self, board: Board) -> int:
        print("The dumb computer is thinking...")
        for i in range(50000000):
            pass
        return random.choice(board.valid_inputs())


class StrategicPlayer(Player):
    def move(self, board: Board) -> int:
        print("The AI CYBORG (╬ Ò ‸ Ó) is thinking...")
        for i in range(100000000):
            pass
        if isinstance(self.winning_move(board), int):
            return self.winning_move(board)
        elif isinstance(self.opponent_winning_move(board), int):
            return self.opponent_winning_move(board)
        # elif fork:
        #     return
        # elif opp_fork:
        #     return
        # elif board.board[5] is None:
        #     return 5
        # elif isinstance(self.opposite_corner(board), int):
        #     return self.opposite_corner(board)
        # elif isinstance(board.empty_corner(), int):
        #     return board.empty_corner()
        # elif isinstance(board.empty_side(), int):
        #     return board.empty_side()
        else:
            return random.choice(board.valid_inputs())

    def winning_move(self, board: Board) -> Optional[int]:
        for valid_input in board.valid_inputs():
            board_copy = copy.deepcopy(board)
            board_copy.move(valid_input, self.char)
            if board_copy.is_straight():
                return valid_input
        return

    def opponent_winning_move(self, board: Board) -> Optional[int]:
        char = 'O' if self.char == 'X' else 'X'
        for valid_input in board.valid_inputs():
            board_copy = copy.deepcopy(board)
            board_copy.move(valid_input, char)
            if board_copy.is_straight():
                return valid_input
        return

    def opposite_corner(self, board: list) -> Optional[int]:
        pass
