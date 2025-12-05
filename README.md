# Hangman Starter Code

Welcome! This README will guide you through using the `hangman-startercode.py` file to build your own Hangman game.

## Table of Contents
1. [Understanding the `pass` Keyword](#understanding-the-pass-keyword)
2. [Strings vs Lists: Key Data Types](#strings-vs-lists-key-data-types)
3. [Reading the Starter Code Comments](#reading-the-starter-code-comments)
4. [What Your Program Should Do](#what-your-program-should-do)
5. [Game Flow and Expected Behavior](#game-flow-and-expected-behavior)

---

## Understanding the `pass` Keyword

### What is `pass`?

The `pass` keyword is a Python placeholder. It does nothing on its own—it's used when Python requires a statement but you don't have any code yet. Think of it as saying "I'll fill this in later."

### Why is it in the starter code?

In Python, if you create a function or add an `if`/`else` block, you **must** have at least one statement inside it. If you leave it blank, you'll get a syntax error and the code won't run at all.

```python
# This won't work - Python will throw an error
def myFunction():

# This will work - pass acts as a placeholder
def myFunction():
    pass
```

### Your job

**Replace `pass` with your actual code.** When you write the function body, your code will replace the `pass` statement entirely. For example:

```python
# Before (what's in the starter code):
def getRandomWord(wordList):
    pass

# After (what you'll write):
def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]
```

---

## Strings vs Lists: Key Data Types

This project uses **strings** and **lists** heavily. Understanding how to work with them is crucial.

### Strings

A **string** is a sequence of characters enclosed in quotes.

```python
name = "alice"
word = "python"
```

**Key operations with strings:**

| Operation | Example | Result |
|-----------|---------|--------|
| **Length** | `len("hello")` | `5` |
| **Indexing** | `"hello"[0]` | `"h"` (first character) |
| **Slicing** | `"hello"[1:4]` | `"ell"` |
| **Check membership** | `"e" in "hello"` | `True` |
| **Concatenation** | `"hello" + " world"` | `"hello world"` |
| **Looping** | `for letter in "abc": print(letter)` | Prints: a, b, c |

**In Hangman, you'll use strings to store:**
- Missed letters: `missedLetters = "aei"` (player guessed a, e, i incorrectly)
- Correct letters: `correctLetters = "olh"` (player guessed o, l, h correctly)

### Lists

A **list** is a sequence of items enclosed in square brackets.

```python
numbers = [1, 2, 3, 4]
fruits = ["apple", "banana", "cherry"]
```

**Key operations with lists:**

| Operation | Example | Result |
|-----------|---------|--------|
| **Length** | `len([1, 2, 3])` | `3` |
| **Indexing** | `[10, 20, 30][1]` | `20` (second item) |
| **Slicing** | `[1, 2, 3, 4][1:3]` | `[2, 3]` |
| **Check membership** | `2 in [1, 2, 3]` | `True` |
| **Looping** | `for item in [1, 2, 3]: print(item)` | Prints: 1, 2, 3 |
| **Append** | `myList.append(4)` | Adds 4 to the end |

**In Hangman, you'll use lists to store:**
- The word list: `words = ['ant', 'baboon', 'badger', ...]`
- The hangman pictures: `HANGMAN_PICS = [picture1, picture2, picture3, ...]`

### Why strings for guesses and lists for collections?

In the starter code, we use **strings** for guessed letters (`"aei"`) and **lists** for collections of words/pictures. This is a design choice that makes certain operations convenient:

- **String for guesses:** It's easy to check if a letter is already guessed: `if "a" in missedLetters:`
- **List for words:** It's easy to randomly select a word: `words[random.randint(0, len(words) - 1)]`

---

## Reading the Starter Code Comments

The starter code uses specific comment types to guide you:

### `# TODO:` Comments

These mark sections you **must implement**. Find every `# TODO:` and replace it with your code.

```python
# TODO: Initialize variables for the game
# You'll need: missedLetters, correctLetters, secretWord, gameIsDone
```

**Your task:** Write the code that initializes these variables.

### Docstrings

Every function has a docstring (text in triple quotes) that explains:
- **What the function does**
- **Parameters** (inputs)
- **Returns** (output)
- **Hints** (clues for implementation)

```python
def getGuess(alreadyGuessed):
    """
    This function prompts the player to guess a letter and validates their input.
    
    Parameters:
        alreadyGuessed: a string containing all letters the player has already guessed
    
    Returns:
        A single lowercase letter that is valid and hasn't been guessed before
    """
    pass
```

**Read these carefully!** They tell you exactly what each function should do.

### Comments inside functions

These explain logic or edge cases you need to handle:

```python
# TODO: Check if the player has won by guessing all letters
# If they won, print a congratulations message and set gameIsDone = True
```

### Provided code

The starter code provides:
- `HANGMAN_PICS`: The ASCII art for hangman stages (don't modify)
- `words`: The word list to choose from (don't modify, but you can if you want)
- Function stubs with docstrings (implement these)

---

## What Your Program Should Do

Your Hangman game should:

1. **Start the game** by choosing a random word from the word list
2. **Display the board** showing:
   - The current hangman picture
   - All missed letter guesses
   - The secret word with guessed letters revealed and blanks (underscores) for unknown letters
3. **Get player input** by prompting for a letter guess with validation:
   - Must be exactly one character
   - Must be a letter (a-z)
   - Cannot be a letter already guessed
4. **Process the guess**:
   - If the letter is in the word → add it to correct letters
   - If the letter is not in the word → add it to missed letters
5. **Check win/loss conditions**:
   - **Win:** Player guesses all letters before running out of guesses
   - **Loss:** Player runs out of guesses (7 missed letters) before finding the word
6. **End the game** and ask if the player wants to play again

---

## Game Flow and Expected Behavior

### Sample Game Session

Here's what a complete game should look like when running:

```
H A N G M A N
  +---+
      |
      |
      |
     ===

Missed letters: 
_ _ _ _ _ _ 
Guess a letter.
e
  +---+
      |
      |
      |
     ===

Missed letters: 
_ _ _ _ e _ 
Guess a letter.
a
  +---+
  O   |
      |
      |
     ===

Missed letters: a 
_ _ _ _ e _ 
Guess a letter.
s
  +---+
  O   |
      |
      |
     ===

Missed letters: a 
_ _ _ _ e s 
Guess a letter.
...
Yes! The secret word is "monkeys"! You have won!
Do you want to play again? (yes or no)
```

### Key Game Mechanics

#### The Board Display
- **Hangman picture:** Changes with each missed guess (7 stages total)
- **Missed letters:** All incorrect guesses shown
- **Secret word:** Shows guessed letters, blanks for unknown

#### Guessing Logic
```
Player guesses → Validate input → Check if in word → Update board → Check win/loss
```

#### Win Condition
The player wins when they've guessed all letters in the secret word before missing 7 times.

#### Loss Condition
The player loses when they've missed 7 guesses (7 wrong letters). When this happens:
- Display the final hangman picture (all 7 stages drawn)
- Reveal the secret word
- Show how many correct and incorrect guesses they made

#### Play Again Loop
After each game ends, ask if they want to play again:
- If **yes** → Reset all variables and start a new game
- If **no** → Exit the program

### Important Details

1. **Case handling:** Convert all guesses to lowercase using the `.lower()` method.
2. **Hangman stages:** The list `HANGMAN_PICS` has 7 pictures (indices 0-6). When `len(missedLetters) == 6`, show the last picture. At `len(missedLetters) == 7`, the game is over.
3. **String building:** To display the secret word with guessed letters revealed, you'll need to:
   - Start with a string of underscores the same length as the secret word
   - Loop through each position in the secret word
   - Check if each letter has been guessed correctly
   - If it has, replace the underscore at that position with the actual letter
   
   You can use string slicing to accomplish this: take the part of the string before the position (`string[:i]`), add the correct letter, then concatenate the part after the position (`string[i+1:]`). This rebuilds the string with one letter revealed at a time.

---

## Next Steps

1. Open `hangman-startercode.py`
2. Read through all the docstrings and comments
3. Implement each function one at a time (start with `getRandomWord`, then `displayBoard`, etc.)
4. Fill in the main game loop
5. Test your game thoroughly!

Good luck! 🎮
