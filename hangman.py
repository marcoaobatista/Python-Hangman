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


def main():
    wrongs = 0
    
    
    wordslist = WORDSLIST['simple']
    i = random.randrange(0, len(wordslist))
    word = wordslist[i]
    
    print(HANGMANPICS[0])
    
    display_lst = ["_"]*len(word)
    print(" ".join(display_lst))
    
    print(word)
    guess = input("\nEnter a guess: ")
    while not guess.isalpha() or len(guess) > 1:
        print(HANGMANPICS[0])
        print(" ".join(display_lst))
        print("\nInvalid input, try again.")
        guess = input("Enter a guess: ")
        
    if guess in word:
        
        print(word.find(guess))
        
    
    
    
    
    
if __name__ == "__main__":
    main()