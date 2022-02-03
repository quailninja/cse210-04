'''This class will be used to store the users guess and make sure it's valid
    Attributes:
        _word (str): taken from ascii_art assigned by director class
        letters_guessed (list): keeps tracks of letters already guessed
        display (str): uses a list to display the word, this allows for _ for letters not yet guessed
'''


class Guess():

    def __init__(self, guess):

        self._guess = guess

    def update_guess(self, letter):

        letter = self.valid_guess(letter)
        self._guess = letter

    def valid_guess(self, letter):
        """Checks to make sure the guess has only one letter
        Args:
            self (Guess): An instance of Guess.
        """
        while len(letter) > 1:
            letter = input("Enter only 1 letter!\nTry again: ")
        while not letter.isalpha():
            letter = input("Only letters(a-z)!\nTry again: ")
        return letter