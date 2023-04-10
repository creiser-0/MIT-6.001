# Problem Set 2, hangman.py
# Name: Creiser
# Time spent: 17 hours

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
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
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
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


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    common_letters = []
    
    for char in secret_word :
        if char in letters_guessed:
            common_letters.append(char)
        else:
            common_letters.append("_ ")
    return "".join(common_letters)


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    available_letters = []
    letters = list(string.ascii_lowercase)
    
    for char in letters:
        if char not in letters_guessed:
            available_letters.append(char)
            
    return "".join(available_letters)
    
def get_input(guess_input, guesses_remaining, warnings_remaining):
    """
    guess_input: need to be an empty string
    guesses_remaining: Current guesses in the game
    warnings_remaining: Current warnings in the game
    returns: A tuple containing:
         [0] = The user valid input string in lower case 
         [1] = The remaining warnings
         [3] = The remaining lifes
    """
    def valid_guess(guess, guesses_remaining, warnings_remaining):
        """
        guess: The string you want to check if its valid for the game
        guesses_remaining: Current guesses in the game
        warnings_remaining: Current warnings in the game
        returns: A tuple containing:
             [0] = The guess string in lower case or an empty string if not valid.
             [1] = The remaining guesses
             [3] = The remaining warnings
         
        If the guess is not valid for the game the remaining warnings get reduced
        by 1, if no warnings are left, remaining guesses get reduced instead.
        """
        if len(guess) != 1:
            print("Please only type 1 letter.")
            return ("", guesses_remaining, warnings_remaining)
        elif not str.isalpha(guess):
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print("Oops! That is not a valid letter. You have", warnings_remaining, 
                      "warnings left.")
            elif guesses_remaining > 0:
                guesses_remaining -= 1
                print("Oops! That is not a valid letter. No warnings left, you have",
                      guesses_remaining, "left.")
            return ("", guesses_remaining, warnings_remaining)
        else:
            guess = str.lower(guess)
            return (guess, guesses_remaining, warnings_remaining)
    while guess_input == "" :
        guess_input = input("please guess a letter: ")
        (guess_input, guesses_remaining , warnings_remaining) = valid_guess(guess_input , guesses_remaining , warnings_remaining)
        return (guess_input, guesses_remaining , warnings_remaining)
    

def check_letter(guess, secret_word, letters_guessed, guesses_remaining, warnings_remaining):
    """
    guess: letter to check if its in secret_word
    secret_word: Word to be guessed
    letter_guessed: List of the letters guessed
    guesses_remaining: Current guesses in the game
    warnings_remaining: current warnings in the game
    returns: -A print message saying if the letter is repeated, not in the 
             secret_word or if the letter is in the word. It also prints the 
             secret_word but with the letters that have not been guessed 
             replaced with underscores(_)
             -tuple containing:
                 [0] = Remaining warnings
                 [1] = Remaining lives
    """
    vowels = "aeiou"
    word = get_guessed_word(secret_word, letters_guessed)
    if guess in letters_guessed:
        if warnings_remaining > 0:
            warnings_remaining -= 1
            print("Oops! You've already guessed that letter. You now have",
                  warnings_remaining ,"warnings.")
        else:
            guesses_remaining -= 1
            print("Oops! You've already guessed that letter. No warnings left. you have",
                  guesses_remaining , "guesses left:")
        return (guesses_remaining , warnings_remaining, word)
    elif guess == " ":
        print("It looks like you dont have no more guesses left.")
        return (guesses_remaining , warnings_remaining)
    letters_guessed.append(guess)
    word = get_guessed_word(secret_word, letters_guessed)
    if guess in secret_word:
        print("Good guess :) :", word)
    elif guess not in vowels:
        guesses_remaining -= 1
        print("Oops! That letter is not in my word:", word)
    else:
        guesses_remaining -= 2
        print("Oops! That letter is not in my word:", word)
    return (guesses_remaining , warnings_remaining, word)

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    letters_guessed = []
    guesses_remaining = 6
    warnings_remaining =  3
    guess_input = ""
    available_letters = get_available_letters(letters_guessed)
    
   
    
    def remainings(guesses_remaining):
        """
        guesses_remaining: Number of guesses left
        warnings_remaining: Number of warnings left
        return: A message with a remainder of the guesses left
        if no guesses left, it ends the game and print a message informing the 
        player that he lose the game and it also print the secret word.
        """
        if guesses_remaining <= 0:
            print("You ran out of guesses. :(\n The word was:", secret_word)
            return False
        print("You have", guesses_remaining, "guesses left.")
        
    def score(guesses_remaining, secret_word):
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
        score = guesses_remaining * len(unique_letters)
        return score

    print("\nWelcome to the Hangman game!\nI am thinking of a word that is", 
          len(secret_word), "letters long.\n-------------------------\nYou have", 
          guesses_remaining, "lives left.\nAvailable letters:", available_letters)
    while not is_word_guessed(secret_word, letters_guessed):
        (guess, guesses_remaininggs, warnings_remaining) = get_input(guess_input, guesses_remaining, warnings_remaining)
        (guesses_remaining, warnings_remaining, word) = check_letter(guess, secret_word, letters_guessed, guesses_remaining, warnings_remaining)
        print("-------------------------\n")
        if remainings(guesses_remaining) == True:
            break
        available_letters = get_available_letters(letters_guessed)
        print("Available letteres:", available_letters)
    
    if guesses_remaining > 0:
        print("Congratulation, you won!\nYour total score for this game is:", 
              score(guesses_remaining, secret_word))



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



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
        return True
    else:
        return False
    
    
def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    possible_matches = []
    for word in wordlist:
        if match_with_gaps(my_word, word):
            possible_matches.append(word)
    if len(possible_matches) == 0:
        print("No matches found.")
    else:
        print(possible_matches)


def get_input_with_hints(guess_input, guesses_remaining, warnings_remaining, my_word):
    """
    guess_input: need to be an empty string
    guesses_remaining: Current guesses in the game
    warnings_remaining: Current warnings in the game
    my_word: string with underscores replacing the letters that have not been guessed
    returns: A tuple containing:
         [0] = The user valid input string in lower case 
         [1] = The remaining warnings
         [3] = The remaining lifes
    """
    def valid_guess(guess, guesses_remaining, warnings_remaining):
        """
        guess: The string you want to check if its valid for the game
        guesses_remaining: Current guesses in the game
        warnings_remaining: Current warnings in the game
        returns: A tuple containing:
             [0] = The guess string in lower case or an empty string if not valid.
             [1] = The remaining guesses
             [3] = The remaining warnings
         
        If the guess is not valid for the game the remaining warnings get reduced
        by 1, if no warnings are left, remaining guesses get reduced instead.
        """
        if guesses_remaining == 0:
            return ("", guesses_remaining, warnings_remaining)
        elif len(guess) != 1:
            print("Please only type 1 letter.")
            return ("", guesses_remaining, warnings_remaining)
        elif guess == "*":
            show_possible_matches(my_word)
            return ("*", guesses_remaining, warnings_remaining)
        elif not str.isalpha(guess):
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print("Oops! That is not a valid letter. You have", warnings_remaining, 
                      "warnings left.")
            elif guesses_remaining > 0:
                guesses_remaining -= 1
                print("Oops! That is not a valid letter. No warnings left, you have",
                      guesses_remaining, "left.")
                return ("", guesses_remaining, warnings_remaining)
        else:
            guess = str.lower(guess)
            return (guess, guesses_remaining, warnings_remaining)
    while guess_input == "" :
        guess_input = input("please guess a letter: ")
        (guess_input, guesses_remaining , warnings_remaining) = valid_guess(guess_input , guesses_remaining , warnings_remaining)
        if guesses_remaining == 0:
            break
        return (guess_input, guesses_remaining , warnings_remaining)

def check_letter_with_hints(guess, secret_word, letters_guessed, guesses_remaining, warnings_remaining):
    """
    guess: letter to check if its in secret_word
    secret_word: Word to be guessed
    letter_guessed: List of the letters guessed
    guesses_remaining: Current guesses in the game
    warnings_remaining: current warnings in the game
    returns: -A print message saying if the letter is repeated, not in the 
             secret_word or if the letter is in the word. It also prints the 
             secret_word but with the letters that have not been guessed 
             replaced with underscores(_)
             -tuple containing:
                 [0] = Remaining warnings
                 [1] = Remaining lives
    """
    vowels = "aeiou"
    word = get_guessed_word(secret_word, letters_guessed)
    if guess == "*" :
        pass
    elif guess in letters_guessed:
        if warnings_remaining > 0:
            warnings_remaining -= 1
            print("Oops! You've already guessed that letter. You now have",
                  warnings_remaining ,"warnings.")
        else:
            guesses_remaining -= 1
            print("Oops! You've already guessed that letter. No warnings left. you have",
                  guesses_remaining , "guesses left:")
        return (guesses_remaining , warnings_remaining, word)
    elif guesses_remaining == 0:
        print("It looks like you dont have no more guesses left.")
        return (guesses_remaining , warnings_remaining, word)
    letters_guessed.append(guess)
    word = get_guessed_word(secret_word, letters_guessed)
    if guess == "*":
        print("There you have some help. ;):", word)
    elif guess in secret_word:
        print("Good guess :) :", word)
    elif guess not in vowels:
        guesses_remaining -= 1
        print("Oops! That letter is not in my word:", word)
    else:
        guesses_remaining -= 2
        print("Oops! That letter is not in my word:", word)
    return (guesses_remaining , warnings_remaining, word)


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    letters_guessed = []
    guesses_remaining = 6
    warnings_remaining =  3
    guess_input = ""
    available_letters = get_available_letters(letters_guessed)
    
    def remainings(guesses_remaining):
        """
        guesses_remaining: Number of guesses left
        warnings_remaining: Number of warnings left
        return: A message with a remainder of the guesses left
        if no guesses left, it ends the game and print a message informing the 
        player that he lose the game and it also print the secret word.
        """
        if guesses_remaining <= 0:
            print("You ran out of guesses. :(\n The word was:", secret_word)
            return False
        else:
            print("You have", guesses_remaining, "guesses left.")
            return True
        
    def score(guesses_remaining, secret_word):
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
        score = guesses_remaining * len(unique_letters)
        return score
    

    print("\nWelcome to the Hangman game!\nI am thinking of a word that is", 
          len(secret_word), "letters long.\n-------------------------\nYou have", 
          guesses_remaining, "lives left.\nAvailable letters:", available_letters)
    while not is_word_guessed(secret_word, letters_guessed):
        my_word = get_guessed_word(secret_word, letters_guessed)
        (guess, guesses_remaininggs, warnings_remaining) = get_input_with_hints(guess_input, guesses_remaining, warnings_remaining, my_word)
        (guesses_remaining, warnings_remaining, my_word) = check_letter_with_hints(guess, secret_word, letters_guessed, guesses_remaining, warnings_remaining)
        print("-------------------------\n")
        if remainings(guesses_remaining) != True:
            break
        available_letters = get_available_letters(letters_guessed)
        print("Available letteres:", available_letters)
    
    if guesses_remaining > 0:
        print("Congratulation, you won!\nYour total score for this game is:", 
              score(guesses_remaining, secret_word))



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
