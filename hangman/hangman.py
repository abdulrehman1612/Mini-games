#====================================
# Assignment 1, hangman.py
# Name: Abdul Rehman
# Roll no: 291223055
# Section: Comp102 (A)
# Time spent: 3-4 hours
#====================================

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    count = 0
    for char in letters_guessed:
        for ch in secret_word:
            if char == ch:
                count+=1
    if count == len(secret_word): #when all secret_word letters are counted in letters_guessed, player won as he guessed all of them
        return True
    else:
        return False


def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    progress_word = ""
    for char in secret_word:
        if char in letters_guessed:
            progress_word += char
        else:
            progress_word += "*"
    
    return progress_word


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    letters = "abcdefghijklmnopqrstuvwxyz"
    available_letters = ""
    for char in letters:
        if char not in letters_guessed:
            available_letters += char
    return available_letters

def reveal_letter(secret_word, available_letters):
    choose_from = ""
    for char in available_letters:
        if char in secret_word:
            choose_from += char
    new = random.randint(0, len(choose_from)-1)
    revealed_letter = choose_from[new]
    return revealed_letter


def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
    print("="*10)
    print("")
    print("Welcome to Hangman!")
    print(f"I am thinking of a word {len(secret_word)} letters long.")
    print("")
    print("-"*10)
    print("")
    guesses_remaining = 10
    letters_guessed = ""
    letters_in_secret_word = ""
    for char in "abcdefghijklmnopqrstuvwxyz":
        if char in secret_word:
            letters_in_secret_word += char
    while guesses_remaining > 0:
        if with_help:
            print(f"You have {guesses_remaining} guesses remaining")
            print(f"Available leters: {get_available_letters(letters_guessed)}")
            guess = input("Please guess a letter: ").lower()
            if (guess in "abcdefghijklmnopqrstuvwxyz!") and len(guess)==1: #check if user gave correct input or not
                if guess == "!": #if user asks for a reveal of letter
                    if guesses_remaining < 3: #check if user has low guesses and asks for a reveal. warns the user once if asking for reveal first time
                        print("You do not have enough guesses for a reveal")
                        print("-"*10)
                        print("")
                    else: #if user has enough guesses for a reveal
                        guess = reveal_letter(secret_word, get_available_letters(letters_guessed))
                        letters_guessed += guess
                        print(f"Letter revealed: {guess}")
                        print(get_word_progress(secret_word, letters_guessed))
                        print("-"*10)
                        print("")
                        guesses_remaining -= 3
                        if has_player_won(secret_word, letters_guessed): #check if player guesses all letters
                            print("Congratulations! You won")
                            print(f"Your total score is: {guesses_remaining+(4*len(letters_in_secret_word))+(3*len(secret_word))}")
                            break
                        elif guesses_remaining < 1: #check if player is out of guesses
                            print(f"Sorry, you ran out of guesses. The word was {secret_word}")
                else: #if user guesses a letter
                    if guess not in letters_guessed: #to check if letter already guessed or not
                        letters_guessed += guess
                        if guess in secret_word: #to check if guess is correct
                            print(f"Good guess: {get_word_progress(secret_word, letters_guessed)}")
                        else: #if guess is incorrect
                            print(f"Opps! That letter is not in my word: {get_word_progress(secret_word, letters_guessed)}")
                        print("-"*10)
                        print("")
                        if has_player_won(secret_word, letters_guessed): #check if player guesses all letters
                            print("Congratulations! You won")
                            print(f"Your total score is: {guesses_remaining+(4*len(letters_in_secret_word))+(3*len(secret_word))}")
                            break
                        if (guess in "aeiou") and (guess not in secret_word): #check if guess was wrong and a vowel
                            guesses_remaining -= 2
                        elif (guess not in "aeiou") and (guess not in secret_word): #check if guess was wrong and a consonant
                            guesses_remaining -= 1
                        if guesses_remaining < 1: #check if player is out of guesses
                            print(f"Sorry, you ran out of guesses. The word was {secret_word}")
                    else: #when guess has already been guessed
                        print("This letter has already been guessed")
                        print("-"*10)
                        print("")
            else:#when guess is not a single alphabet from a-z
                print("Invalid input! Have a look at available letters and only enter one character at a time.")
                print("-"*10)
                print("")
        else:
            print(f"You have {guesses_remaining} guesses remaining")
            print(f"Available leters: {get_available_letters(letters_guessed)}")
            guess = input("Please guess a letter: ").lower()
            if (guess in "abcdefghijklmnopqrstuvwxyz") and len(guess)==1: #check if user gave correct input or not
                if guess not in letters_guessed: #to check if letter already guessed or not
                    letters_guessed += guess
                    if guess in secret_word: #to check if guess is correct
                        print(f"Good guess: {get_word_progress(secret_word, letters_guessed)}")
                    else: #if guess is incorrect
                        print(f"Opps! That letter is not in my word: {get_word_progress(secret_word, letters_guessed)}")
                    print("-"*10)
                    print("")
                    if has_player_won(secret_word, letters_guessed): #check if player guesses all letters
                        print("Congratulations! You won")
                        print(f"Your total score is: {guesses_remaining+(4*len(letters_in_secret_word))+(3*len(secret_word))}")
                        break
                    if (guess in "aeiou") and (guess not in secret_word): #check if guess was wrong and a vowel
                        guesses_remaining -= 2
                    elif (guess not in "aeiou") and (guess not in secret_word): #check if guess was wrong and a consonant
                        guesses_remaining -= 1
                    if guesses_remaining < 1: #check if player is out of guesses
                        print(f"Sorry, you ran out of guesses. The word was {secret_word}")
                else: #when guess has already been guessed
                    print("This letter has already been guessed")
                    print("-"*10)
                    print("")
            else:#when guess is not a single alphabet from a-z
                    print("Invalid input! Have a look at available letters and only enter one character at a time.")
                    print("-"*10)
                    print("")
            
    



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

     secret_word = choose_word(wordlist)
     with_help = True
     hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your assignment. However, please run test_a1_student.py
    # one more time before submitting to make sure all the tests pass.
    

