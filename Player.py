class Player:
    """

    """
    _name: str
    _char: str

    def __init__(self, name: str, char: str):
        """Initialises the player.
        """
        self._name = name
        self._char = char

    def change_name(self, new_name: str):
        """

        :param new_name:
        :return:
        """
        self._name = new_name
