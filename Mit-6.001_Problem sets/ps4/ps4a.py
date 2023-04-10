# Problem Set 4A
# Name: Creiser
# Collaborators: GOD (again)
# Time Spent: 0:45 

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    # Base case
    if len(sequence) <= 1:
        return sequence
   
    
    else:
        #create an empty list to store all the combinations
        combinations = []  
        #   get_permutations(sequence[1:]) returns a list of all the permutations of 
        #   the sequence without the first character
        for permutation in get_permutations(sequence[1:]): 
            # the range is the length of the string + 1 because adding 1 
            # character at the end of the string its also a new string
            for i in range(len(permutation)+1):
                new_combination = permutation[0:i] + sequence[0] + permutation[i:]
                if new_combination not in combinations:
                # this if its only to avoid repeated permutations 
                    combinations.append(new_combination)
        return combinations


# if __name__ == '__main__':
    #EXAMPLE
    # example_input = 'abc'
    # print('Input:', example_input)
    # print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    # print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)
    # print(get_permutations("aeiou"))
    # first_case = 'fab'
    # print('Input:', first_case)
    # print('Expected Output:', ['fab', 'fba', 'afb', 'abf', 'bfa', 'baf'])
    # print('Actual Output:', get_permutations(first_case))
    # second_case = 'lol'
    # print('Input:', second_case)
    # print('Expected Output:', ['lol', 'oll', 'llo'])
    # print('Actual Output:', get_permutations(second_case))
    # third_case = 'shi'
    # print('Input:', third_case)
    # print('Expected Output:', ['shi', 'sih', 'his', 'hsi', 'ish', 'ihs'])
    # print('Actual Output:', get_permutations(third_case))
