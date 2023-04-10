# Problem Set 4C
# Name: Creiser
# Collaborators: this time we are here with Lady Gaga
# Time Spent: 1:00 

import string
from ps4a import get_permutations

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
        
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words.copy()
                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        vowels_permutation_upper = vowels_permutation.upper()
        vowels_permutation_lower = vowels_permutation.lower()
        #Create 2 varibales to prevent any errors if the initial string isnt all lower case
        mapping_dict = {}
        
        for i in range(5):
            mapping_dict[VOWELS_LOWER[i]] = vowels_permutation_lower[i]
            mapping_dict[VOWELS_UPPER[i]] = vowels_permutation_upper[i]
            # With the order of the vowel always been "aeiou" we can map all the letters
            # in only 5 iterations, the loop maps the originall letter with the permutation letter
        
        return mapping_dict
    
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        encrypted_message = []
        for character in self.message_text:
            if character in VOWELS_LOWER or character in VOWELS_UPPER:
                encrypted_message.append(transpose_dict[character])
            # If a character is a Vowel it adds to the list the permuted vowel in the dict,
            # otherwise adds the character to the list
            else:
                encrypted_message.append(character)
                
        return "".join(encrypted_message)
        #returns a string containing the encrypted message
        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        SubMessage.__init__(self, text)

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        VOWELS_permutations = get_permutations(VOWELS_LOWER) 
        
        valid_words_dictionary = {}
        #the dictionary stores the quantity of valid words with the combination of vowels that was used
        
        for permutation in VOWELS_permutations:
            valid_words = 0
            mapping_dict = self.build_transpose_dict(permutation)
            Decrypted_message = self.apply_transpose(mapping_dict)
            Decrypted_message = Decrypted_message.split()
            for word in Decrypted_message:
                if is_word(self.valid_words, word):
                    valid_words += 1
            valid_words_dictionary[valid_words] = permutation 
        
        most_valid_words = max(valid_words_dictionary.keys())
        
        if most_valid_words >= 1:
            best_permutation = valid_words_dictionary[most_valid_words]
            best_transpose = self.build_transpose_dict(best_permutation)
            Decrypted_message = self.apply_transpose(best_transpose)
            #decrypting the message recovering the permutation with most valid words
            #and using that permutation to decrypt the message
            return Decrypted_message
        else:
            return self.message_text
        
if __name__ == '__main__':
    
    # Example test case
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
     
    #TODO: WRITE YOUR TEST CASES HERE 
    #test case 1
    test1 = SubMessage("We are talking english")
    permutation1 = "oeaiu"
    test1_dict = test1.build_transpose_dict(permutation1)
    print("Original value:", test1.message_text, "Permutation:", permutation1)
    test1_encrypted = test1.apply_transpose(test1_dict)
    print("Encrypted message:", test1_encrypted)
    
    #test case 2
    test2 = SubMessage("UPPER LETTERS ONLY :v")
    permutation2 = "euaoi"
    test2_dict = test2.build_transpose_dict(permutation2)
    print("Original value:", test2.message_text, "Permutation:", permutation2)
    test2_encrypted = test2.apply_transpose(test1_dict)
    print("Encrypted message:", test2_encrypted)
    
    #test case 3
    test3  = test1_encrypted
    test3 = EncryptedSubMessage(test3)
    print("Encrypted message:", test3.message_text)
    test3_decrypted = test3.decrypt_message()
    print("Decrypted message:", test3_decrypted)

    #test case 4
    
    test4  = test2_encrypted
    test4 = EncryptedSubMessage(test4)
    print("Encrypted message:", test4.message_text)
    test4_decrypted = test4.decrypt_message()
    print("Decrypted message:", test4_decrypted)
