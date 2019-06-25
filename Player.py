import Board


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
        valid = False
        while not valid:
            position = input(f'{self.name} make a move! ')
            position = int(position)
            if not board.valid(position):
                print('Invalid input. Choose another position...')
            else:
                valid = True
        return position
