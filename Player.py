import Board
import random


class Player:
    """

    """
    name: str
    char: str

    def __init__(self, name: str, char: str):
        """Initialises the player.
        """
        self.name = name
        self.char = char

    def move(self, board: Board):
        raise NotImplementedError


class UserPlayer(Player):
    def move(self, board: Board):
        valid = False
        while not valid:
            position = input(f'{self.name} make a move! ')
            print(board.valid_inputs())
            position = int(position)
            if position not in board.valid_inputs():
                print('Invalid input. Choose another position...')
            else:
                valid = True
        return position


class RandomPlayer(Player):
    def move(self, board: Board):
        print("The computer is thinking...")
        for i in range(65000000):
            pass
        return random.choices(board.valid_inputs())[0]


class StrategicPlayer(Player):
    def move(self, board: Board):
        raise NotImplementedError
