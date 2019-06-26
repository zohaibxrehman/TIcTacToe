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
    print('AI CYBORG (☞◣д◢)☞:  A')
    print('=======================')

    valid_type = False
    while not valid_type:
        user_type = input(f'Enter the type for {generic_name}: ')
        if user_type == 'H' or user_type == 'h':
            name = input(f'Enter a name for human {generic_name}: ')
            player = HumanPlayer(name, char)
            valid_type = True
        elif user_type == 'C' or user_type == 'c':
            name = 'Computer'
            player = ComputerPlayer(name, char)
            valid_type = True
        elif user_type == 'A' or user_type == 'a':
            name = 'AI CYBORG (☞◣д◢)☞'
            player = CyborgPlayer(name, char)
            valid_type = True
        else:
            print("Invalid key for user type! Please refer to the "
                  "USER TYPE TABLE and try again.")
    print('')
    return player


def main() -> None:
    """Play multiple rounds of a TIC-TAC-TOE based on user input settings.
    """
    print("=== TIC-TAC-TOE ===\n\n")
    p1 = make_player('player 1', 'X')
    p2 = make_player('player 2', 'O')
    if (isinstance(p1, ComputerPlayer) and isinstance(p2, ComputerPlayer)) or \
        (isinstance(p1, CyborgPlayer) and isinstance(p2, CyborgPlayer)):
        p1.name = p1.name + ' 1'
        p2.name = p2.name + ' 2'

    while True:
        game = TicTacToe((p1, p2))
        winner = game.play()

        if winner is None:
            print('Game tied!')
        else:
            print(f'And the winner is  {winner.name}!!! \n')
            winner.wins += 1
        again = input(f'{p1.name} and {p2.name}, would you like to play again? '
                      f'(y/n)')
        print('')
        if again != 'y' and again != 'Y':
            print(f'{p1.name} won {p1.wins} times!')
            print(f'{p2.name} won {p2.wins} times!')
            print('GAME OVER!')
            return None


if __name__ == '__main__':
    main()
