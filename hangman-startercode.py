import random

# This data structure is provided for you - don't modify it
HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''']

# This word list is provided for you - you do not need to modify it, but may if you wish.
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()


# TODO: Implement this function
def getRandomWord(wordList):
    """
    This function takes a list of words and returns a random word from that list.
    
    Parameters:
        wordList: a list of strings
    
    Returns:
        A randomly selected string from wordList
    """
    pass # Replace this line with your code


# TODO: Implement this function
def displayBoard(missedLetters, correctLetters, secretWord):
    """
    This function displays the current state of the game, including:
    - The hangman picture based on missed letters
    - The list of missed letters
    - The secret word with guessed letters revealed and blanks for unknown letters
    
    Parameters:
        missedLetters: a string containing all missed letter guesses
        correctLetters: a string containing all correct letter guesses
        secretWord: the word that the player is trying to guess
    
    Returns:
        None (just prints output)
    
    Hint: Use HANGMAN_PICS[len(missedLetters)] to get the appropriate hangman picture
    """
    pass


# TODO: Implement this function
def getGuess(alreadyGuessed):
    """
    This function prompts the player to guess a letter and validates their input.
    Keep asking until the player enters:
    - A single character
    - A letter (a-z)
    - A letter they haven't already guessed
    
    Parameters:
        alreadyGuessed: a string containing all letters the player has already guessed
    
    Returns:
        A single lowercase letter that is valid and hasn't been guessed before
    """
    pass


# TODO: Implement this function
def playAgain():
    """
    This function asks the player if they want to play again.
    
    Returns:
        True if the player wants to play again, False otherwise
        (Hint: check if their answer starts with 'y')
    """
    pass


# Main game loop - YOU NEED TO COMPLETE THIS
print('H A N G M A N')

# TODO: Initialize variables for the game
# You'll need: missedLetters, correctLetters, secretWord, gameIsDone
# Think about what values these should start with and assign them


while True:
    # TODO: Display the current board
    
    # TODO: Get the player's guess
    # Remember to pass in alreadyGuessed letters (both missed and correct)
    
    # TODO: Check if the guess is in the secret word
    if True:  # REPLACE THIS CONDITION
        # TODO: Add the guess to correctLetters
        
        # TODO: Check if the player has won by guessing all letters
        # If they won, print a congratulations message and set gameIsDone = True
        pass
    else:
        # TODO: Add the guess to missedLetters
        
        # TODO: Check if the player has lost (too many missed guesses)
        # If they lost, display the board and print a game over message, then set gameIsDone = True
        pass
    
    # TODO: Ask if they want to play again (only if the game is done)
    # If yes, reset variables and continue playing
    # If no, break out of the loop
