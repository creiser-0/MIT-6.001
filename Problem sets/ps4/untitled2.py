# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 20:47:55 2023

@author: creis
"""

VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'


def build_transpose_dict(vowels_permutation):
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
    mapping_dict = {}
    
    for i in range(5):
        mapping_dict[vowels_permutation_lower[i]] = VOWELS_LOWER[i]
        mapping_dict[vowels_permutation_upper[i]] = VOWELS_UPPER[i]
    
    return mapping_dict


dictionary = build_transpose_dict("eioau")
