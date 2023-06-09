"""
prompt for a difficulty
choose a random word in the list

"""


import random

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
    
    def check_win(self):
        pass
    
    def display(self):
        print(HANGMANPICS[self.wrongs])
    
    def get_guess(self):
        pass
    
    def make_guess(self):
        pass


def main():
    wrongs = 0
    
    wordslist = WORDSLIST['simple']
    i = random.randrange(0, len(wordslist))
    word = wordslist[i]
    display_lst = ["_"]*len(word)
    previous_guesses = set()
    
    while True:
        print(HANGMANPICS[wrongs])
        
        print(" ".join(display_lst))
        
        # loop until guess is valid
        guess = input("\nEnter a guess: ")
        while not guess.isalpha() or len(guess) > 1:
            print(HANGMANPICS[wrongs])
            print(" ".join(display_lst))
            print("\nInvalid input, try again.")
            guess = input("Enter a guess: ")
        
        # if user has already guessed this letter, continue
        if guess in previous_guesses:
            print("You've already guessed that, try again")
            continue
        previous_guesses.add(guess)
        
        for i,ch in enumerate(word):
            if ch == guess:
                display_lst[i] = guess
        
        if guess not in word:
            wrongs += 1
        
        if wrongs == 5 or display_lst.count("_") == 0:
            break
            
    
    
    
    
if __name__ == "__main__":
    main()