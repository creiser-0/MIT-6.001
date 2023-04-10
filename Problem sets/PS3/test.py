# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 00:29:55 2023

@author: creis
"""

# def match_with_gaps(word, other_word):
#     '''
#     word: string with 1 characters replaced with *
#     other_word: string, regular English word
#     returns: boolean, True if all the actual letters of word match the 
#         corresponding letters of other_word, or the letter is the special symbol
#         * , and word and other_word are of the same length;
#         False otherwise: 
#     '''
#     word_copy = word.replace(" ", "")
#     common_letters = []
    
#     if len(word_copy) != len(other_word):
#         return False

#     for i, letter in enumerate(word_copy):
#         if letter == other_word[i]:
#             common_letters.append(letter)
#         elif letter == "*":
#             common_letters.append("*")
    
#     if common_letters == list(word_copy) :
#         return True
#     else:
#         return False
    
# VOWELS = "aeiou"
# word = "c*ws"
# # print(word[1])
# # print("cows" == "cows")
# # print(match_with_gaps("c*wsr", "cows"))


# word_with_vowel = []
 
# for vowel in VOWELS:
#     word_with_vowel.append(word.replace("*", vowel))

x = "pedro"
y = x
print(x)
print(y)

y = y[1:2]