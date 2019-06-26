import Board
import random
from typing import Optional
import copy
import time


class Player:
    """
    Superclass for all types of players.

    === Attributes ===
    name:
        name of the player
    char:
        the character played by the player in tic-tac-toe, 'X' or 'O'
    wins:
        number of wins in tic-tac-toe
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


class HumanPlayer(Player):
    """
    The human player.

     === Attributes ===
    name:
        name of the player
    char:
        the character played by the player in tic-tac-toe, 'X' or 'O'
    wins:
        number of wins in tic-tac-toe
    """
    name: str
    char: str
    wins: int

    def move(self, board: Board) -> int:
        """Return a keypad position played by the human on the <board>.
        """
        valid = False
        while not valid:
            position = input(f'{self.name} make a move: ')
            position = int(position)
            if position not in board.valid_inputs():
                print('Invalid input. Choose another position...\n')
            else:
                valid = True
        print('')
        return position


class ComputerPlayer(Player):
    """
    A not-too-smart computer player.

     === Attributes ===
    name: name of the player
    char: the character played by the player in tic-tac-toe, 'X' or 'O'
    wins: number of wins in tic-tac-toe
    """
    name: str
    char: str
    wins: int

    def move(self, board: Board) -> int:
        """Return a keypad position played by the computer on the <board>.
        """
        print(f'{self.name} is thinking...')
        time.sleep(1)
        if isinstance(self.winning_move(board), int):
            return self.winning_move(board)
        else:
            return random.choice(board.valid_inputs())

    def winning_move(self, board: Board) -> Optional[int]:
        """Return a winning keypad position if it exists on the <board>;
        else None
        """
        for valid_input in board.valid_inputs():
            board_copy = copy.deepcopy(board)
            board_copy.move(valid_input, self.char)
            if board_copy.is_straight():
                return valid_input
        return


class CyborgPlayer(ComputerPlayer):
    """
    A smart computer player that seeks nothing but victory.

     === Attributes ===
    name: name of the player
    char: the character played by the player in tic-tac-toe, 'X' or 'O'
    wins: number of wins in tic-tac-toe
    """
    name: str
    char: str
    wins: int

    def move(self, board: Board) -> int:
        """Return a keypad position played by the computer on the <board>.
        """
        print(f'{self.name} is thinking...')
        time.sleep(1.75)
        # if board.is_empty():
        #     # not necessary but can mess up bad players more
        #     # algorithm will slightly diff if want to do this
        #     return random.choice([1, 3, 7, 9])
        if isinstance(self.winning_move(board), int):
            return self.winning_move(board)
        elif isinstance(self.opponent_winning_move(board), int):
            return self.opponent_winning_move(board)
        elif isinstance(self.fork(board), int):
            return self.fork(board)
        elif isinstance(self.opponent_fork(board), int):
            return self.opponent_fork(board)
        elif board[5] is None:
            return 5
        elif isinstance(self.opposite_corner(board), int):
            return self.opposite_corner(board)
        elif isinstance(board.empty_corner(), int):
            return board.empty_corner()
        elif isinstance(board.empty_side(), int):
            return board.empty_side()
        else:
            return random.choice(board.valid_inputs())

    def opponent_winning_move(self, board: Board) -> Optional[int]:
        """Return a winning keypad position if it exists on the <board> for the
        opponent; else None.
        """
        opp_char = 'O' if self.char == 'X' else 'X'
        for valid_input in board.valid_inputs():
            board_copy = copy.deepcopy(board)
            board_copy.move(valid_input, opp_char)
            if board_copy.is_straight():
                return valid_input
        return

    def fork(self, board: Board) -> Optional[int]:
        """Return a keypad position which creates an opportunity where the player
        has two ways to win.
        """
        opp_char = 'O' if self.char == 'X' else 'X'
        for valid_input in board.valid_inputs():
            board_copy = copy.deepcopy(board)
            board_copy.move(valid_input, self.char)
            if isinstance(self.winning_move(board_copy), int):
                board_copy.move(self.winning_move(board_copy), opp_char)
                if isinstance(self.winning_move(board_copy), int):
                    return valid_input
        return

    def opponent_fork(self, board: Board) -> Optional[int]:
        opp_char = 'O' if self.char == 'X' else 'X'
        count = 0
        for valid_input in board.valid_inputs():
            board_copy = copy.deepcopy(board)
            board_copy.move(valid_input, opp_char)
            if isinstance(self.opponent_winning_move(board_copy), int):
                board_copy.move(self.opponent_winning_move(board_copy),
                                self.char)
                if isinstance(self.opponent_winning_move(board_copy), int):
                    best_move = valid_input
                    count += 1
        if count == 1:
            return best_move
        elif count > 1:
            # TODO
            return
        else:
            return

    def opposite_corner(self, board: Board) -> Optional[int]:
        """Return a keypad corner position opposite to an opponent's corner
        if it is empty; else None.
        """
        opp_char = 'O' if self.char == 'X' else 'X'
        if (board[7] is opp_char and board[3] is None) or \
                (board[7] is None and board[3] is opp_char):
            return 7 if board[7] is None else 3
        elif (board[1] is opp_char and board[9] is None) or \
                (board[1] is None and board[9] is opp_char):
            return 9 if board[9] is None else 1
        else:
            return
