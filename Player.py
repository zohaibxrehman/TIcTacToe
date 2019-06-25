import Board
import random
from typing import Union


class Player:
    """

    """
    name: str
    char: str

    def __init__(self, name: str, char: str) -> None:
        """Initialises the player.
        """
        self.name = name
        self.char = char

    def move(self, board: Board) -> int:
        raise NotImplementedError


class UserPlayer(Player):
    def move(self, board: Board) -> int:
        valid = False
        while not valid:
            position = input(f'{self.name} make a move! ')
            position = int(position)
            if position not in board.valid_inputs():
                print('Invalid input. Choose another position...\n')
            else:
                valid = True
        return position


class RandomPlayer(Player):
    def move(self, board: Board) -> int:
        print("The dumb computer is thinking...")
        for i in range(65000000):
            pass
        return random.choices(board.valid_inputs())[0]


class ComputerPlayer(Player):
    def move(self, board: Board) -> int:
        if isinstance(self.winning_move(board.board), int):
            return self.winning_move(board.board)
        elif isinstance(self.opponent_winning_move(board.board), int):
            return board.opponent_winning_move
        # elif fork:
        #     return
        # elif opp_fork:
        #     return
        elif board.board[5] is None:
            return 5
        elif isinstance(self.opposite_corner(board.board), int):
            return self.opposite_corner()
        elif isinstance(board.empty_corner(), int):
            return board.empty_corner()
        elif isinstance(board.empty_side(), int):
            return board.empty_side()
        else:
            return random.choice(board.valid_inputs())[0]

    def winning_move(self, board: list) -> Union[int, None]:
        pass

    def opponent_winning_move(self, board: list) -> Union[int, None]:
        pass

    def opposite_corner(self, board: list) -> Union[int, None]:
        pass





class StrategicPlayer(Player):
    def move(self, board: Board) -> int:
        raise NotImplementedError
