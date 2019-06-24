from Board import Board
import Player
from typing import Union


class TicTacToe:
    """

    """
    board: Board
    players: tuple
    turn: int
    _invalid: list

    def __init__(self, players: tuple):
        self.board = Board()
        self.players = players
        self.turn = 0
        self._invalid = []

    def play(self) -> Union[str, None]:
        """Play one round of this NumberGame. Return the name of the winner.

        A "round" is one full run of the game, from when the count starts
        at 0 until the goal is reached.
        """
        while not self.board.is_straight() or not self.board.is_full():
            self.play_one_turn()
        # The player whose turn would be next (if the game weren't over) is
        # the loser. The one who went one turn before that is the winner.
        if not self.board.is_straight():
            winner = None
        else:
            winner = self.whose_turn(self.turn - 1).name
        return winner

    def play_one_turn(self) -> None:
        """
        """
        player = self.whose_turn(self.turn)
        valid = False
        while not valid:
            position = input(f'{player.name} make a move! ')
            position = int(position)
            if position in self._invalid:
                print('Invalid input. Choose another position...')
            else:
                valid = True
                self._invalid.append(position)

        self.board.move(position, player.char)
        self.turn += 1

        # print(f'{next_player.name} moves {amount}.')

    def whose_turn(self, turn: int) -> Player:
        """Return the Player whose turn it is on the given turn number.
        """
        if turn % 2 == 0:
            return self.players[0]
        else:
            return self.players[1]

