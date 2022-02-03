from game.word import Word
import game.ascii_art as art
import random as r
from game.guess import Guess
from game.jumper import Jumper
import os


class Director:
    """A person who directs the game.

    The responsibility of a Director is to control the sequence of play.
    Attributes:
        word (str): random word from a list from ascii
        game_on (boolean): Whether or not the game is being played.
        jumper (int): Players current life
        guess (str): The players current guess.
    """

    def __init__(self):
        """Constructs a new Director.

        Args:
            self (Director): an instance of Director.
        """
        self.word = Word(r.choice(art.fourth_grade_words))
        self.jumper = Jumper(6)
        self.guess = Guess("Nil")
        self.game_on = True

    def start_game(self):
        """Starts the game by running the main game loop.

        Args:
            self (Director): an instance of Director.
        """
        print(f"{art.logo_jumper}\nThe word has {len(self.word._word)} letters")
        input("Press Enter to Continue")
        while self.game_on:
            self.get_inputs()
            self.update_board()
            self.check_win()

    def get_inputs(self):
        """Just runs the word class to check guesses
        Args:
            self (Director): An instance of Director.
        """
        print(f"{self.jumper.jump_man}\n{' '.join(self.word.display)}\nLetters Guessed: {' '.join(self.word.letters_guessed)}\nLives Remaining: {self.jumper._lives}")
        self.guess.update_guess(input("Guess a letter: "))

    def update_board(self):
        """Update the board information to display to the user
        Args:
            self (Director): An instance of Director.
        """
        os.system("cls" if os.name == "nt" else "clear")
        if self.guess._guess not in self.word._word and self.guess._guess not in self.word.letters_guessed:
            self.jumper.update_lives()
        self.word.check_guess(self.guess._guess)

    def check_win(self):
        """Checks to see if the game was won
        Args:
            self (Director): An instance of Director.
        """
        if "_" in self.word.display and self.jumper._lives < 1:
            self.game_on = False
            print(f"{art.game_over}\nThe word was {self.word._word}")
        elif "_" not in self.word.display and self.jumper._lives > 0:
            self.game_on = False
            print(art.winner)
        else:
            pass