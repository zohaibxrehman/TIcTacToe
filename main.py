import Board
import Player
from typing import Tuple

class TicTacToe:
    """

    """
    board: Board
    players: Tuple[Player, Player]
    turn: int


    def __init__(self):
        self.board = Board()
        self.player1 = Player()
        self.player2 = Player()

    def start(self):
        print('Hello there! What is your name?')


    def make_a_move(self):

    def end(self):


def make_player(generic_name: str) -> Player:
    """Return a new Player based on user input.

    Allow the user to choose a player name and player type.
    <generic_name> is a placeholder used to identify which player is being made.
    """
    name = input(f'Enter a name for {generic_name}: ')
    player = Player(name)
    # valid_type = False
    # print(f'You have three options for the type of player {name}')
    # print('===USER TYPE TABLE===')
    # print('User Player:          U')
    # print('Computer:             C')
    # print('Strategic Computer:   S')
    # print('=====================')
    # while not valid_type:
    #     type = input(f'Enter the type of player for {name}: ')
    #     if type == 'U' or type == 'u':
    #         player = UserPlayer(name)
    #         valid_type = True
    #     elif type == 'C' or type == 'c':
    #         player = RandomPlayer(name)
    #         valid_type = True
    #     elif type == 'S' or type == 's':
    #         player = StrategicPlayer(name)
    #         valid_type = True
    #     else:
    #         print("Invalid key for User type. Please refer to the USER TYPE TABLE and try again!")
    return player

def main() -> None:
    p1 = make_player('p1')
    p2 = make_player('p2')
    while True:
        game = TicTacToe((p1, p2))
        winner = game.play()
        print(f'And {winner} is the winner!!!')
        print(p1)
        print(p2)
        again = input('Again? (y/n) ')
        if again != 'y':
            return
        


if __name__ == '__main__':
    main()
