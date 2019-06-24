from TicTacToe import TicTacToe
from Player import Player


def make_player(generic_name: str, char: str) -> Player:
    """Return a new Player based on user input.

    Allow the user to choose a player name and player type.
    <generic_name> is a placeholder used to identify which player is being made.
    """
    name = input(f'Enter a name for {generic_name}: ')
    player = Player(name, char)
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
    #         print("Invalid key for User type. Please refer to the USER TYPE
    #         TABLE and try again!")
    return player


def main() -> None:
    p1 = make_player('p1', 'X')
    p2 = make_player('p2', 'Y')
    while True:
        game = TicTacToe((p1, p2))
        winner = game.play()
        if winner is None:
            print('Game tied!')
        else:
            print(f'And the winner is  {winner}!!!')
        print(f'{p1.name} and {p2.name}, would you like to play again?')
        again = input('Again? (y/n) ')
        if again != 'y':
            return


if __name__ == '__main__':
    main()
