# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 23:03:36 2023

@author: creis
"""
import string

    
def check_guess (secret_word, letters_guessed):
    """
    Parameters
    ----------
    secret_word : STRING
    Word to be guessed 
    letters_guessed : LIST
    list of the characters guessed
    
    Returns: Boolean
    -------
    check if all the letters in secret_word are in letters_guessed, only works
    if all letters are in lower case
    """
    secret_word_list = []
    for char in secret_word:
        secret_word_list.append(char)
        
    common_letters = []
    
    for char in secret_word :
        if char in letters_guessed:
            common_letters.append(char)
    if sorted(secret_word_list) == sorted(common_letters):
        return True
    else:
        return False
    
def get_guessed_word (secret_word, letters_guessed):
    """
    Parameters
    ----------
    secret_word : STRING
        Word to be guessed 
    letters_guessed : LIST
        list of the letters guessed
    
    Returns: Boolean
    -------
    A string with the letters that have been guessed revealed and those that 
    not appear as an underscore (_)
    """
    
    common_letters = []
    
    for char in secret_word :
        if char in letters_guessed:
            common_letters.append(char)
        else:
            common_letters.append("_ ")
    return "".join(common_letters)

def get_available_letters (letters_guessed) :
    """
    Parameters
    ----------
    letters_guessed : LIST
        The list of letters that have been guessed

    Returns
    -------
    A string with all the letters that have not been used

    """
    available_letters = []
    letters = list(string.ascii_lowercase)
    
    for char in letters:
        if char not in letters_guessed:
            available_letters.append(char)
            
    return "".join(available_letters)

def valid_guess(guess, remaining_warnings, remaining_lives):
    """
    guess: The string you want to check if its valid for the game
    remaining_warnings: Current Warnings in the game
    remaining_lives: Current lives in the game
    returns: A tuple containing:
        [0] = The guess string in lower case or an empty string if not valid.
        [1] = The remaining warnings
        [3] = The remaining lifes
    
    If the guess is not valid for the game the remaining warnings get reduced
    by 1, if no warnings are left, remaining lives get reduced instead.
    """
    if len(guess) != 1:
        print("Please only type 1 letter.")
        return ("", remaining_warnings, remaining_lives)
    elif not str.isalpha(guess):
        if remaining_warnings > 0:
            remaining_warnings -= 1
            print("Oops! That is not a valid letter. You have", remaining_warnings, 
              "warnings left.")
        elif remaining_lives > 0:
            remaining_lives -= 1
            print("Oops! That is not a valid letter. No warnings left, you have",
                  remaining_lives, "left.")
        else:
            return (" ", remaining_warnings, remaining_lives)
        return ("", remaining_warnings, remaining_lives)
    else:
        guess = str.lower(guess)
        return (guess, remaining_warnings, remaining_lives)
            
def get_input(guess_input, remaining_warnings, remaining_lives):
    """
    guess_input: need to be an empty string
    remaining_warnings: Current Warnings in the game
    remaining_lives: Current lives in the game
    returns: A tuple containing:
        [0] = The user valid input string in lower case 
        [1] = The remaining warnings
        [3] = The remaining lifes
    """
    while guess_input == "" :
        guess_input = input("please guess a letter: ")
        (guess_input, remaining_warnings, remaining_lives) = valid_guess(guess_input , remaining_warnings, remaining_lives)
    return (guess_input, remaining_warnings, remaining_lives)

def check_letter(guess, secret_word, letters_guessed, remaining_warnings, remaining_lives):
    """
    guess: letter to check if its in secret_word
    secret_word: Word to be guessed
    letter_guessed: List of the letters guessed
    remaining_warnings: Current Warnings in the game
    remaining_lives: Current lives in the game
    returns: -A print message saying if the letter is repeated, not in the 
             secret_word or if the letter is in the word. It also prints the 
             secret_word but with the letters that have not been guessed 
             replaced with underscores(_)
             -tuple containing:
                 [0] = Remaining warnings
                 [1] = Remaining lives
    """
    vowels = "aeiou"
    if guess in letters_guessed:
        if remaining_warnings > 0:
            remaining_warnings -= 1
            print("Oops! You've already guessed that letter. You now have",
                  remaining_warnings,"warnings.")
        else:
            remaining_lives -= 1
            print("Oops! You've already guessed that letter. No warnings left. you have",
                  remaining_lives, "lives left:")
        return (remaining_warnings, remaining_lives)
    elif guess == " ":
        print("It looks like you dont have no more lifes left.")
        return (remaining_warnings, remaining_lives)
    letters_guessed.append(guess)
    word = get_guessed_word(secret_word, letters_guessed)
    if guess in secret_word:
        print("Good guess :) :", word)
    elif guess not in vowels:
        remaining_lives -= 1
        print("Oops! That letter is not in my word:", word)
    else:
        remaining_lives -= 2
        print("Oops! That letter is not in my word:", word)
    return (remaining_warnings, remaining_lives)

def score(remaining_lives, secret_word):
    """
    remaining_lives: remaining lives at the end of the game.
    secret_word: word to be guessed.
    return: return the total score for the current game based in the formula:
        Total score = guesses_remaining* number unique letters in secret_word
    """
    unique_letters = []    
    for letter in secret_word:
        if letter not in unique_letters:
            unique_letters.append(letter)
    score = remaining_lives * len(unique_letters)
    return score

def hangman(secret_word):
    """
    secret_word: Word to be guessed
    Interactive game based in the hangman game where you have to guess a word 
    with only letters, the only info you have at the begining is the lenght of 
    the word after the first guess if the letter is in the word you get that 
    letter revealed in the word, word that are not yet guessed appear as "_"
    Rules:
        -you have 6 guesses and 3 warnings
        -if you guess a letter that was already used you lose 1 warning
        -if you guess a vowel that is not in the word you lose 2 guesses
        -if you guess a constant letter that is not in the word you lose 1 guess
        -you can only use alphabet letters, if you try to use another type of
         letter you lose 1 warning
        -if you dont have more warnings left you lose 1 guess instead
        -if you dont have anymore guesses you lose the game
    """
    letters_guessed = []
    remaining_lives = 6
    remaining_warnings =  3
    guess_input = ""
    available_letters = get_available_letters(letters_guessed)
    
    def remainings(remaining_warnings,remaining_lives,):
        if remaining_lives <= 0:
            print("You ran out of lives. :(\n The word was:", secret_word)
            return True
        print("You have", remaining_lives, "lives left.")
        

    print("\nWelcome to the Hangman game!\nI am thinking of a word that is", 
          len(secret_word), "letters long.\n---------------------------------------\nYou have", 
          remaining_lives, "lives left.\nAvailable letters:", available_letters)
    while not check_guess(secret_word, letters_guessed):
        (guess, remaining_warnings, remaining_lives) = get_input(guess_input, remaining_warnings, remaining_lives)
        (remaining_warnings, remaining_lives) = check_letter(guess, secret_word, letters_guessed, remaining_warnings, remaining_lives)
        print("-------------------------\n")
        if remainings(remaining_warnings, remaining_lives) == True:
            break
        available_letters = get_available_letters(letters_guessed)
        print("Available letteres:", available_letters)
    
    if remaining_lives > 0:
        print("Congratulation, you won!\nYour total score for this game is:", 
              score(remaining_lives, secret_word))
    

    
def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word = str.strip(my_word)
    other_word = str.strip(other_word)
    my_word_copy = list(my_word.replace(" ", ""))
    common_letters = []
    
    if len(my_word_copy) != len(other_word):
        return False

    for char in range(len(my_word_copy)):
        if my_word_copy[char] in other_word[char]:
            common_letters.append(my_word_copy[char])
        else:
            common_letters.append("_")
    
    if common_letters == my_word_copy:
        print(common_letters)
        print(my_word_copy)
        return True
    else:
        print(common_letters)
        print(my_word_copy)
        return False
str.replace
word1 = "_ _ t t"
word2 = "tart"
# w3 = str.strip(word1)
# print(w3)
print(match_with_gaps(word1, word2))