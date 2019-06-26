from Board import Board
from Player import Player
from typing import Optional
from Visualizer import visualizer


class TicTacToe:
    """
    The classic tic-tac-toe game for two players.
    First player to get three in a row wins.

    The game can have multiple rounds.

    === Attribute ===
    board:
        3x3 board on which the game is played
    players:
        the two players
    turn:
        The turn the game is on, beginning with turn 0.
        If turn is even number, it is players[0]'s turn.
        If turn is any odd number, it is player[1]'s turn.
    """
    board: Board
    players: tuple
    turn: int

    def __init__(self, players: tuple) -> None:
        """Initialises the game.
        """
        self.board = Board()
        self.players = players
        self.turn = 0
        self._invalid = []

    def play(self) -> Optional[Player]:
        """Play one round of TicTacToe. Return the name of the winner.

        A "round" is one full run of the game.
        """
        visualizer(self.board)
        while not self.board.is_straight() and not self.board.is_full():
            self.play_one_turn()
        if not self.board.is_straight():
            winner = None
        else:
            winner = self.whose_turn(self.turn - 1)
        return winner

    def play_one_turn(self) -> None:
        """Play a single turn in the game.

        Determine whose move it is, get their move, and update the board
        as well as the number of the turn we are on.
        """
        player = self.whose_turn(self.turn)

        position = player.move(self.board)
        self.board.move(position, player.char)

        self.turn += 1

        visualizer(self.board)

    def whose_turn(self, turn: int) -> Player:
        """Return the Player whose turn it is on the given turn number.
        """
        if turn % 2 == 0:
            return self.players[0]
        else:
            return self.players[1]
