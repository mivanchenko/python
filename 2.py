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
    >>> print(count('banana', 'b'))
    1
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

#count_ok_words = 0
#fin = open('words.txt')
#for line in fin:
#    word = line.strip()
#    i = 0
#    count = 0
#    while i < len(word)-1:
#        if word[i] == word[i+1]:
#            count += 1
#            if count == 3:
#                print(word)
#            i += 2
#        else:
#            count = 0
#            i += 1

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

t = [[1], 2, [[3]]]
#print(nested_sum(t))

from collections import Iterable

def flatten(items, ignore_types=(str, bytes)):
    """Yield items from any nested iterable; see REF."""
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x

#print(list(flatten(l)))
#for x in flatten(l):
#    print(x)

def is_abecedarian_for(word):
    prev_letter = 'a'
    for letter in word:
        if letter < prev_letter:
            return False
        prev_letter = letter
    return True

def is_abecedarian_while(word):
    i = 0
    while i < len(word) - 1:
        if word[i] > word[i+1]:
            return False
        i += 1
    return True

def is_abecedarian_recurse(word):
    if len(word) <= 1:
        return True
    if word[0] > word[1]:
        return False
    return is_abecedarian(word[1:])

word = 'abcderf'

def wrap(func, *args):
    def wrapped():
        return func(*args)
    return wrapped

wrap_is_abecedarian_for     = wrap(is_abecedarian_for, word)
wrap_is_abecedarian_while   = wrap(is_abecedarian_while, word)
wrap_is_abecedarian_recurse = wrap(is_abecedarian_recurse, word)

import timeit

#print(timeit.timeit(wrap_is_abecedarian_for    , number=10000))
#print(timeit.timeit(wrap_is_abecedarian_while  , number=10000))
#print(timeit.timeit(wrap_is_abecedarian_recurse, number=10000))

def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res

#print("abc".capitalize())
#print(''.join(capitalize_all('abc')))

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

#print(cumul([1, 2, 3]))

def middle(t):
    '''Returns a new list containing all but the first and the last elements.

    >>> print(middle([1, 2, 3, 4]))
    [2, 3]
    '''

    return t[1:-1]

def chop(t):
    '''Modifies the list by removing the first and the last elements.
       Returns None.

    >>> print(chop([1, 2, 3, 4]))
    None
    '''

    t.pop()
    del t[0]

import doctest
doctest.testmod()

#t = [1, 2, 3, 4]
#print(middle(t))
#print(t)

#t = [1, 2, 3, 4]
#print(chop(t))
#print(t)

import random

choice = random.choice(['apple', 'pear', 'banana'])
#print(choice)

sample = random.sample(range(100), 10)
#print(sample)

#print('ok') if 0 else print(2)

words = dict()
fin = open('words.txt')
for line in fin:
    line = line.strip()
    words[line] = 1

#print(len(words))

#word = input('Enter a word: ')
#print(word) if word in words else print('No such word')

def histogram(s):
    d = dict()
    for c in s:
#        if c not in d:
#            d[c] = 1
#        else:
#            d[c] += 1
#        c = d.get(c, 1)
        d[c] = d.get(c, 0) + 1
    return d

#print(histogram('alfa romeo'))

def print_hist(h):
    l = list()
    for k in h:
        l.append(k)
    l.sort()
    for k in l:
        print(k, h[k])

h = histogram('parrot')
#print_hist(h)

def reverse_lookup(d, v):
    l = list()
    for k in d:
        if d[k] == v:
            l.append(k)
#            return k
#    raise ValueError('value does not appear in a dict')
    l.sort()
    return l

#print(reverse_lookup(h, 3))

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
#        if val not in inverse:
#            inverse[val] = [key]
#        else:
#            inverse[val].append(key)
        inverse.setdefault(val, [])
        inverse[val].append(key)
    return inverse

#print(histogram('parrot'))
#print(invert_dict(histogram('parrot')))

def invert_dict2(d):
    inverse = dict()
    for k, v in d.items():
        inverse[v] = k
    return inverse

#print(invert_dict2(histogram('parrot')))

known = {0:0, 1:1}

def example():
#    global known
    known[0] = 42
#    known = list()

#print(known)
#example()
#print(known)

import pprint

stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
stuff.insert(0, stuff[:])
pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(stuff)
pp = pprint.PrettyPrinter(width=41, compact=True)
#pp.pprint(stuff)

tup = ('spam', ('eggs', ('lumberjack', ('knights', ('ni', ('dead', ('parrot',
('fresh fruit',))))))))
pp = pprint.PrettyPrinter(depth=6)
#pp.pprint(tup)

d = dict()
d[(42,)] = 1234
#print(d)

def sumall(*args):
    return sum(args)
#    a_sum = 0
#    for a in args:
#        a_sum += a
#    return a_sum

#print(sum((2, 3, 4)))
#print(sumall(2, 3, 4))

t1 = (1, 2, 3, 4)
t2 = (0, 1, 3, 5)

#for x, y in zip(t1, t2):
#    if x == y:
#        print(x)

#for index, element in enumerate('abc'):
#    print(index, element)

directory = {
    ('Cleese', 'John'): 42,
    ('Vleese', 'Bohn'): 43,
    ('Bleese', 'Zohn'): 44,
}
#print(directory)

#for last, first in directory:
#    print(first, last)
#for last in directory:
#    print(last)
#for last, first in directory:
#    print(first, last, directory[last, first])

def sort_by_length(words):
    t = []
    for word in words:
       t.append((len(word), word))
    t.sort(reverse=True)
    res = []
    for length, word in t:
        res.append(word)
    return res

import random
def sort_by_length_2(words):
    t = []
    for word in words:
       t.append((len(word), random.random(), word))
    t.sort(reverse=True)
    res = []
    for length, _, word in t:
        res.append(word)
    return res

def sorted_dict(words):
    sorted_words = words[:]
    sorted_words.sort(reverse=True)
    sorted_words = enumerate(sorted_words)
    sorted_dict = dict()
    for i, s in sorted_words:
        sorted_dict[s] = i
    return sorted_dict

def sort_by_length_3(words):
    t = []
    sort_dict = sorted_dict(words)
    for word in words:
       t.append((len(word), sort_dict[word], word))
    t.sort(reverse=True)
    res = []
    for length, _, word in t:
        res.append(word)
    return res

words = []
fin = open('words.txt')
i = 0
for l in fin:
    l = l.strip()
    words.append(l)
    if i >= 20:
        break
    i += 1
#words = sort_by_length(words)
#words = sort_by_length_2(words)
#words = sort_by_length_3(words)
#print(words)

#t = ['a', 'b', 'c']
#print(t)
#t.reverse()
#print(t)
#
#print(sorted(t))
#t2 = (*reversed(t),)
#print(t2)
#t2 = tuple(reversed(t))
#print(t2)
#t2 = tuple(reversed(t),)
#print(t2)
#t2 = list(reversed(t))
#print(t2)

#s = 'abc'
#print(s)
#t = list(s)
#print(t)

def most_frequent(s):
    freq = dict()
    for l in s:
        freq[l] = freq.get(l, 0) + 1
    ls = list()
    for l in freq:
        ls.append((freq[l], l))
    ls.sort(reverse=True)
#    print(ls)
    for t in ls:
        print(t[0], '=>', t[1])

#most_frequent('banana eats apple')

#print(callable(most_frequent))
#print(callable(most_frequent('')))
#print(callable(random.random))

###

def signature(w):
    t = list(w)
    t.sort()
    return ''.join(t)

def build_anagrams_set():
    words = dict()
    fin = open('words.txt')
    for line in fin:
        word = line.strip().lower()
        sig = signature(word)
        if sig not in words:
            words[sig] = [word]
        else:
            words[sig].append(word)
    return words

def print_anagrams(anagrams):
    for sig, words in anagrams.items():
        if len(words) > 1:
            print(words)

anagrams = build_anagrams_set()
#print_anagrams(anagrams)

def anagrams_by_size(anagrams):
    a_by_size = []
    for sig, words in anagrams.items():
        if len(words) > 1:
            a_by_size.append((len(words), words))
    a_by_size.sort(reverse=True)
    return a_by_size

sized_anagrams = anagrams_by_size(anagrams)
#for a in sized_anagrams:
#    print(a)

def anagrams_of_length(anagrams, n):
    a_of_len = []
    for sig, words in anagrams.items():
        if len(words) > 1 and len(sig) == n:
            a_of_len.append((len(words), words))
    a_of_len.sort(reverse=True)
    return a_of_len

len_anagrams = anagrams_of_length(anagrams, 8)
print(len_anagrams[0])
#for a in len_anagrams:
#    print(a)

