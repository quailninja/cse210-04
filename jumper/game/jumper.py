import game.ascii_art as aa

'''This class will be used to store lives of user and jump man graphic
    Attributes:
        _live (int): number of lives remaining
        jump_man (str): the graphic used for ascii_art in it's different stages
'''


class Jumper():

    def __init__(self, lives):

        self._lives = lives
        self.jump_man = aa.easy_stage[self._lives]

    def update_lives(self):
        """Updates life and jump man graphic
        Args:
            self (Jumper): An instance of Jumper.
        """
        self._lives -= 1
        self.jump_man = aa.easy_stage[self._lives]