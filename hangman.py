"""
############################################################
# 
# Hangman Game
# 
# Algorithm (main)
#     Display welcome banner
#     while the user wants to continue
#         prompt for difficulty
#         start game
#         get game status
#         while the game is not over
#             display hangman and letters
#             prompt for a guess
#             log that guess
#             get game status
#         display hangman and letters
#         print game result
#         prompt if user wants to continue
#     display goodbye message
# 
############################################################
"""

import random

BANNER = """
 __      __   _                    _         _  _                                
 \ \    / /__| |__ ___ _ __  ___  | |_ ___  | || |__ _ _ _  __ _ _ __  __ _ _ _  
  \ \/\/ / -_) / _/ _ \ '  \/ -_) |  _/ _ \ | __ / _` | ' \/ _` | '  \/ _` | ' \ 
   \_/\_/\___|_\__\___/_|_|_\___|  \__\___/ |_||_\__,_|_||_\__, |_|_|_\__,_|_||_|
                                                           |___/                                                                                                        
"""

HANGMANPICS = [
    """
  ____
 |/   |
 |    
 |    
 |    
_|_
========
""",
    """
  ____
 |/   |
 |    O
 |   
 |   
_|_
========
""",
    """
  ____
 |/   |
 |    O
 |    |
 |    
_|_
========
""",
    """
  ____
 |/   |
 |    O
 |   /|
 |   
_|_
========
""",
    """
  ____
 |/   |
 |    O
 |   /|\\
 |   
_|_
========
""",
    """
  ____
 |/   |
 |    O
 |   /|\\
 |   / 
_|_
========
""",
    """
  ____
 |/   |
 |    O
 |   /|\\
 |   / \\
_|_
========
"""]


WORDSLIST = {
    'simple': [
        'dog', 'cat', 'hat', 'sun', 'bird',
        'house', 'shoe', 'bed', 'tree', 'book'
    ],
    'intermediate': [
        'rainbow', 'banana', 'elephant', 'computer',
        'strawberry', 'telescope', 'halloween',
        'sandwich', 'butterfly', 'pancake'
    ],
    'advanced': [
        'hippopotamus', 'cryptocurrency', 'unbelievable',
        'astrophysics', 'quintessential', 'pneumonia',
        'uncharacteristically', 'entrepreneurship',
        'individualistic', 'electromagnetic'
    ]
}


class Hangman(object):
    def __init__(self, dificulty):
        self.dificulty = dificulty
        self.wrongs = 0

        wordslist = WORDSLIST[dificulty]

        # get random word index
        i = random.randrange(0, len(wordslist))
        self.word = wordslist[i]

        self.display_lst = ["_"]*len(self.word)
        self.previous_guesses = set()

    def get_status(self):
        """ Returns the current status of the game, if the game has ended, 
and if the player has won or lost or neither 
        return: game_ended, result (tuple)
        """
        if self.wrongs == 6:
            return True, "lost"
        elif self.display_lst.count("_") == 0:
            return True, "won"
        return False, ""

    def display(self):
        """ 
        Displays the current hangman, letters, and wrong guesses 
        return: None
        """
        print(HANGMANPICS[self.wrongs])
        print(" ".join(self.display_lst))
        print("\nWrong guesses: ", end="\n")
        for letter in self.previous_guesses - set(self.word):
            print(letter, end=" ")
        print()

    def get_guess(self):
        """ 
        Prompts for a guess and reprompts if it is not valid or if user has
already guessed that letter 
        return: None
        """
        self.guess = input("\nEnter a guess: ")
        # reprompt if invalid
        while not self.guess.isalpha() or len(self.guess) > 1:
            self.display()
            print("\nInvalid input, try again.")
            self.guess = input("Enter a guess: ")

        # if user has already guessed this letter, re-prompt
        if self.guess in self.previous_guesses:
            print("\nYou've already guessed that, try again")
            self.get_guess()
        self.previous_guesses.add(self.guess)

    def log_guess(self):
        """ 
        Adds guess to the list if it is correct and record miss if it is not
        return: None
        """
        # add guess to list
        for i, ch in enumerate(self.word):
            if ch == self.guess:
                self.display_lst[i] = self.guess

        if self.guess not in self.word:
            self.wrongs += 1

    def reveal_word(self):
        """
        Displays the word
        return: None
        """
        print("\nThe word was", self.word.upper())


def get_difficulty():
    """ 
    Prompts for a difficulty s,i or a and reprompt, invalid and returns 
equivalent to input
    return: difficulty (string)
    """
    valid_dificulties = {"s": "simple", "i": "intermediate", "a": "advanced"}
    prompt = """\nCHOOSE A DIFFICULTY
simple, intermediate or advanced (s, i, a): """
    answer = input(prompt)
    
    while answer.lower() not in valid_dificulties:
        print("\nInvalid dificulty, try again")
        answer = input(prompt)
    return valid_dificulties[answer.lower()]


def main():
    print(BANNER)
    cont = "y"
    while cont.lower() == "y":
        difficulty = get_difficulty()
        game = Hangman(difficulty)
        game_ended, result = game.get_status()

        while not game_ended:
            game.display()
            game.get_guess()
            game.log_guess()
            game_ended, result = game.get_status()

        game.display()
        print("\nGAME", result.upper())
        game.reveal_word()
        cont = input("\nDo you want to play again? (y/n) ")

    print("\nThanks for playing! :)")


if __name__ == "__main__":
    main()
