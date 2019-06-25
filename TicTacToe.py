from Board import Board
from Player import Player
from typing import Optional
from Visualizer import visualizer


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

    def play(self) -> Optional[Player]:
        """Play one round of TicTacToe. Return the name of the winner.

        A "round" is one full run of the game.
        """
        while not self.board.is_straight() and not self.board.is_full():
            visualizer(self.board)
            self.play_one_turn()
        # The player whose turn would be next (if the game weren't over) is
        # the loser. The one who went one turn before that is the winner.
        visualizer(self.board)
        if not self.board.is_straight():
            winner = None
        else:
            winner = self.whose_turn(self.turn - 1)
        return winner

    def play_one_turn(self) -> None:
        """
        """
        player = self.whose_turn(self.turn)

        position = player.move(self.board)
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
