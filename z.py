def average(values):
    '''Computes the averages.

    >>> print(average([20, 30, 70]))
    40.0
    '''

    return sum(values) / len(values)

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

#    count = 0
#    for letter in a_word:
#        if letter == a_letter:
#            count += 1
#    return count

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

def is_reverse(word1, word2):
    '''Returns True if the second word is the reversed version of the first
    one.

    >>> print(is_reverse('rbbr', 'rbbr'))
    True
    >>> print(is_reverse('rbbr', 'abba'))
    False
    >>> print(is_reverse('pots', 'stop'))
    True

    '''
    if len(word1) != len(word2):
        return False
    i = 0
    j = len(word2) - 1
    while j >= 0:
#        print(i, j)
        if word1[i] != word2[j]:
            return False
        i += 1
        j -= 1
    return True

def avoids(word, forbidden_letters):
    '''Returns True if the word does not use any of the forbidden letters.

    >>> print(avoids('banana', 's'))
    True
    >>> print(avoids('banana', 'so'))
    True
    >>> print(avoids('banana', 'sob'))
    False
    >>> print(avoids('banana', 'b'))
    False
    >>> print(avoids('banana', 'ba'))
    False
    >>> print(avoids('banana', 'bar'))
    False

    '''

    for f in forbidden_letters:
        if f in word:
            return False
    return True

def uses_only(word, only_letters):
    '''Returns True if a word uses only letters in the list.

    >>> print(uses_only('banana', 'ban'))
    True
    >>> print(uses_only('banana', 'band'))
    True
    >>> print(uses_only('banana', 'ba'))
    False
    '''

    for letter in word:
        if letter not in only_letters:
            return False
    return True

def uses_all(word, required_letters):
    '''Returns True if a word uses all the required letters at least once.

    >>> print(uses_all('banana', 'ban'))
    True
    >>> print(uses_all('banana', 'band'))
    False
    '''

    return uses_only(required_letters, word)

def is_abecedarian(word):
    '''Returns True if a word appear in alphabetical order.

    >>> print(is_abecedarian('abcde'))
    True
    >>> print(is_abecedarian('abbcdde'))
    True
    >>> print(is_abecedarian('aa'))
    True
    >>> print(is_abecedarian('acbde'))
    False
    '''

    prev_letter = 'a'
    for letter in word:
        if letter < prev_letter:
            return False
        prev_letter = letter
    return True

#    i = 0
#    while i < len(word) - 1:
#        if word[i] > word[i+1]:
#            return False
#        i += 1
#    return True

#    if len(word) <= 1:
#        return True
#    if word[0] > word[1]:
#        return False
#    return is_abecedarian(word[1:])

def nested_sum(t):
    '''Returns the sum of the elements in a list.

    >>> print(nested_sum([1, 2, 3]))
    6
    >>> print(nested_sum([[1], 2, [[3]]]))
    6
    >>> print(nested_sum(['1', '2', '3']))
    123
    '''

    if isinstance(t[0], type(t)):
        t[0] = nested_sum(t[0])
    if len(t) == 1:
        return t[0]
    return t[0] + nested_sum(t[1:])

def cumul(t):
    '''Returns the list of cumulative sums from the given list.

    >>> print(cumul([1, 2, 3]))
    [1, 3, 6]
    '''

    c = []
    i = 0
    sum = 0
    while i < len(t):
        sum += t[i]
        c.append(sum)
        i += 1
    return c

import doctest
doctest.testmod()

