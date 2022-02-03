'''This class will be used to store the word for the player and keep track of letters guessed
    Attributes:
        _word (str): taken from ascii_art assigned by director class
        letters_guessed (list): keeps tracks of letters already guessed
        display (str): uses a list to display the word, this allows for _ for letters not yet guessed
'''


class Word():

    def __init__(self, word):

        self._word = word
        self.letters_guessed = []
        self.display = ["_" for x in self._word]

    def check_guess(self, guess):
        """Checks the users guess to see if it's in the word or if it's already been guessed before
        Args:
            self (Word): An instance of Word.
        """
        if guess not in self._word and guess not in self.letters_guessed:
            self.letters_guessed.append(guess)
            print(f"{guess} is not in the word.")
        elif guess in self.display or guess in self.letters_guessed:
            print(f"You've already guessed: {guess}")
        for x in range(len(self._word)):
            if guess == self._word[x]:
                self.display[x] = guess