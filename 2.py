#!/usr/bin/env python3

def repeat_lyrics():
    print_lyrics()
    print_lyrics()
def print_lyrics():
    print(1)
    print(2)
#repeat_lyrics()

fruit = 'banana'
index = 0
#while index < len(fruit):
#    zindex = len(fruit) - 1 - index
#    print(fruit[zindex], end='')
#    index += 1
#print()

#for char in fruit:
#    print(char, end='')
#print()

prefixes = 'JKLMNOPQ'
suffix = 'ack'

#for letter in prefixes:
#    print(letter, end='')
#    if letter in ('O', 'Q'):
#        print('u', end='')
#    print(suffix)

def find(word, letter, start):
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
    >>> print(count('banana', 'n'))
    2
    '''

    count = 0
    for letter in a_word:
        if letter == a_letter:
            count += 1
    return count

def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False
    i = 0
    j = len(word2) - 1
    while j >= 0:
        print(i, j)
        if word1[i] != word2[j]:
            return False
        i += 1
        j -= 1
    return True

#print(is_reverse('pots', 'stop'))

count, e_count = 0, 0
fin = open('words.txt')
for l in fin:
    l = l.strip()
    if len(l) >= 20:
#        print(l)
        count += 1
        if 'e' in l:
            e_count += 1
#print(count)
#print(e_count)
#print(round( (count - e_count) / count * 100 ))

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

#def uses_all(word, required_letters):
#    '''Returns True if a word uses all the required letters at least once.
#
#    >>> print(uses_all('banana', 'ban'))
#    True
#    >>> print(uses_all('banana', 'band'))
#    False
#    '''
#
#    for letter in required_letters:
#        if letter not in word:
#            return False
#    return True

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

#    prev_letter = 'a'
#    for letter in word:
##        if ord(letter) < ord(prev_letter):
#        if letter < prev_letter:
#            return False
#        prev_letter = letter
#    return True

#    # exit condition
#    if len(word) <= 1:
#        return True
#    # working condition
#    if word[0] > word[1]:
#        return False
#    # dive into recursion
#    return is_abecedarian(word[1:])

    i = 0
    while i < len(word) - 1:
        if word[i] > word[i+1]:
            return False
        i += 1
    return True

import doctest
doctest.testmod()

#forbidden_letters = input('Enter the string of forbidden letters: ')
#print(forbidden_letters)
#count_ok_words = 0
#fin = open('words.txt')
#for line in fin:
#    word = line.strip()
#    if avoids(word, forbidden_letters):
#        print('.', end='')
#        count_ok_words += 1
#print(count_ok_words)

#allowed_letters = 'acefhlo'
#count_ok_words = 0
#fin = open('words.txt')
#for line in fin:
#    word = line.strip()
#    if uses_only(word, allowed_letters):
#        print(word, end=' ')
#        count_ok_words += 1
#print(count_ok_words)

#required_letters = 'aeiouy'
#count_ok_words = 0
#fin = open('words.txt')
#for line in fin:
#    word = line.strip()
#    if uses_all(word, required_letters):
#        print(word)
#        count_ok_words += 1
#print(count_ok_words)

#count_ok_words = 0
#fin = open('words.txt')
#for line in fin:
#    word = line.strip()
#    if is_abecedarian(word):
##        print('.', end='')
##        print(word, end=' ')
#        count_ok_words += 1
#print(count_ok_words)

count_ok_words = 0
fin = open('words.txt')
for line in fin:
    word = line.strip()
    i = 0
    count = 0
    while i < len(word)-1:
        if word[i] == word[i+1]:
            count += 1
            if count == 3:
                print(word)
            i += 2
        else:
            count = 0
            i += 1


