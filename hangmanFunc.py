# For use in hangman.py

# This function prints list as if it is a string
def printlst(list):
    for item in list:
        print(item, end="")


# converts a list to string
def lstToStr(list):
    tempStr = ""
    for letter in list:
        tempStr += letter
    return tempStr.upper()


# To create same number of underscores as the chosen word
def mask(word):
    templst = []
    for letter in word:
        templst += "_"
    return templst


# To remove body parts of the game character using the number of wrong answers
def cutbody(livesConsumed):
    stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

    return stages[livesConsumed]

def title():
    hangmanTitle = """
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
    """
    return hangmanTitle