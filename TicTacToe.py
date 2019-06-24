from Board import Board
import Player
# from typing import Tuple


class TicTacToe:
    """

    """
    board: Board
    players: tuple
    turn: int

    def __init__(self, players: tuple):
        self.board = Board()
        self.players = players
        self.turn = 0

    def play(self) -> str:
        """Play one round of this NumberGame. Return the name of the winner.

        A "round" is one full run of the game, from when the count starts
        at 0 until the goal is reached.
        """
        while not self.board.is_straight():
            self.play_one_turn()
        # The player whose turn would be next (if the game weren't over) is
        # the loser. The one who went one turn before that is the winner.
        winner = self.whose_turn(self.turn - 1)
        return winner.name

    def play_one_turn(self) -> None:
        """
        """
        player = self.whose_turn(self.turn)
        print(f'{player.name} make a move!')
        position = int(input('Coordinate: '))
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

