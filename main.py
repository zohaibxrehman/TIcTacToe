from TicTacToe import TicTacToe
from Player import *


def make_player(generic_name: str, char: str) -> Player:
    """Return a new Player based on user input.

    Allow the user to choose a player name and player type.
    <generic_name> is a placeholder used to identify which player is being made.
    """
    print('====USER TYPE TABLE====')
    print('Human Player:         H')
    print('Computer:             C')
    print('Strategic Computer:   S')
    print('=======================')

    # player = Player(name, char)

    valid_type = False
    while not valid_type:
        user_type = input(f'Enter the type for {generic_name}: ')
        if user_type == 'H' or user_type == 'h':
            name = input(f'Enter a name for human {generic_name}: ')
            player = UserPlayer(name, char)
            valid_type = True
        elif user_type == 'C' or user_type == 'c':
            name = 'Computer'
            player = RandomPlayer(name, char)
            valid_type = True
        elif user_type == 'S' or user_type == 's':
            name = 'AI CYBORG (╬ Ò ‸ Ó)'
            player = StrategicPlayer(name, char)
            valid_type = True
        else:
            print("Invalid key for user type. Please refer to the "
                  "USER TYPE TABLE and try again!")
    print('')
    return player


def main() -> None:
    print("=== TIC-TAC-TOE ===\n\n")
    p1 = make_player('player 1', 'X')
    p2 = make_player('player 2', 'Y')
    while True:
        game = TicTacToe((p1, p2))
        winner = game.play()
        if winner is None:
            print('Game tied!')
        else:
            print(f'And the winner is  {winner}!!! \n')
        again = input(f'{p1.name} and {p2.name}, would you like to play again? '
                      f'(y/n)')
        if again != 'y' and again != 'Y':
            return


if __name__ == '__main__':
    main()
