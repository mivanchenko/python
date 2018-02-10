def average(values):
    '''Computes the averages.

    >>> print(average([20, 30, 70]))
    40.0
    '''

    return sum(values) / len(values)

def find(word, letter, start=0):
    '''Finds the letter in a string.

    Returns the position found.

    >>> print(find('bananas', 'a', 2))
    3
    >>> print(find('bananas', 'a', 1))
    1
    '''

    index = start
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1
    return -1

def count(a_word, a_letter):
    '''Counts the number of times a letter appears in a string.

    >>> print(count('banana', 'a'))
    3
    >>> print(count('banana', 'b'))
    1
    >>> print(count('banana', 'n'))
    2
    '''

    count = 0
    pos = 0
    while pos > -1:
        pos = find(a_word, a_letter, pos)
        if pos > -1:
            pos += 1
            count += 1
    return count

import doctest
doctest.testmod()

