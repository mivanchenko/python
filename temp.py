#!/usr/bin/env python

#print('{}' 'Py' 'thon')
#print(
#    'Put several strings within parentheses '
#    'to have them joined together.'
#)

#a = ['Mary', 'had', 'a', 'little', 'lamb']
##for i in range(len(a)):
##    print(i, a[i])
#
#b = enumerate(a)
#for elem in b:
#    print(elem[0], elem[1])

##def concat(*args, sep='/'):
#def concat(sep='/', *args):
#    return sep.join(args)
#
#print(concat('earth', 'mars', 'venus'))

#print(list(range(3, 6)))
#args = [3, 6]
#print(list(range(*args)))

#args = {'dog', 'cat', 'bat'}
#shmargs = (*args,)
#print(shmargs)

#pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
#pairs.sort(key = lambda i: i[1])
#print(pairs)

#from collections import deque
#
#q = deque(["Eric", "John", "Michael"])
#q.append("Terry")
#q.popleft()
#print(q)

#squares = []
#x = 42
#print(x)
#for x in range(10):
#    squares.append(x**2)
#print(squares)
#print(x)

#x = 42
#print(x)
#squares = list(map(lambda x: x**2, range(10)))
#print(squares)
#print(x)

#x = 42
#print(x)
#squares = [x**2 for x in range(10)]
#print(squares)
#squares = [x**2 for x in range(10) if x > 5]
#print(squares)
#print(x)

#matrix = [
#    [1, 2, 3],
#    [4, 5, 6],
#    [7, 8, 9],
#]
#
#print(list(zip(*matrix)))

#a = set('abracadabra')
#b = set('alacazam')
#print(a)
#print(b)
#c = list(a-b)
##c = [a-b]
#c.sort()
#print(c)
#print(sorted(a-b))

#d = {'q': 'w', 'a': 's', 'z': 'x'}
#print(d.keys())
#print(list(d.keys()))
#print(sorted(d.keys()))

#d = dict({1: 2})
#print(d)
#
#d = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
#print(d)
#
#d = dict((('sape', 4139), ('guido', 4127), ('jack', 4098)))
#print(d)
#
#d = {x: x**2 for x in range(6)}
#print(d)
#
#d = dict(sape = 4139, guido = 4127)
#print(d)

#knights = {'gallahad': 'the pure', 'robin': 'the brave'}
#for k, v in knights.items():
#    print(k, v)

#for i, v in enumerate(['tic', 'tac', 'toe']):
#    print(i, v)

#questions = ['name', 'quest', 'favourite color']
#answers = ['lancelot', 'the holy grail', 'blue']
#for q, a in zip(questions, answers):
#    print('What is your {}? It is {}'.format(q, a))

#basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
#for f in sorted(set(basket)):
#    print(f)

#print('Українська' > 'Русский')
#print('Українська' == 'Русский')
#print('Українська' < 'Русский')

## '!a' apply ascii(), '!s' apply str(), '!r' apply repr()
#contents = 'eelsґ'
#print('My hovercraft is full of {!a}.'.format(contents))

#table = { 'k1': 11, 'k2': 22, 'k3': 33 }
#print('K1: {0[k1]:d}; K2: {0[k2]:d}; K3: {0[k3]:d}'.format(table))
#print('K1: {k1:d}; K2: {k2:d}; K3: {k3:d}'.format(**table))

#with open('workfile') as f:
#    read_data = f.read()
#print(f.closed)

#with open('poem.txt') as f:
#    for line in f:
#        print(line, end='')

#with open('poem.txt') as f:
#    lines1 = list(f)
#    lines1 = lines1[::-1]
#    print(lines1)
#    print(f.tell())
#    f.seek(0)
#    lines2 = f.readlines()
#    lines2 = sorted(lines2, reverse=True)
##    lines2 = lines2[::-1]
#    print(lines2)

#with open('workfile', 'w') as f:
#    value = ('the answer', 42)
#    s = str(value)
#    f.write(s)

import json

#json1 = json.dumps( [1, 'simple', 'list'] )
#print(json1)
#
#with open('workfile', 'w') as f:
#    json.dump(json1, f)
#    f.write('\n')

#with open('workfile') as f:
#    x = json.load(f)
#    print(x)

from random import randint

#cons = ['b', 'd']
#print(len(cons))
#for i in range(0, 3):
#    con = cons[randint(0, len(cons) - 1)]
#    word = 'a' + con + 'i' + con + 'as'
#    print(word)

#class A:
#    def m1(self):
#        print('m1')
#
#a = A()
#a.m1()
##a.m1 = 42
##a.m1()
##print(a.m1)
#
#print([].__class__)
#print('42'.__class__)
#print(int(42).__class__)
#
#print(a.m1.__self__)
#print(a.m1.__func__)

#data = ['a', 'b', 'c']
#print(len(data))
#
#for r in range(len(data), -1, -1):
#    print(r)

#table = {x: x*2 for x in range(1, 5)}
#print(table)

import os

#for root, dirs, files, rootfd in os.fwalk('/home/michael/pe/python'):
#   print(root, "consumes", end=" ")
#   print(sum([os.stat(name, dir_fd=rootfd).st_size for name in files]),
#         end=" ")
#   print("bytes in", len(files), "non-directory files")
#   if '.git' in dirs:
#       dirs.remove('.git')  # don't visit git directories

#print(os.getenv('PWD'))
#os.renames('oldfile', 'newfile')

#import shutil
#
#shutil.copyfile('newfile', 'oldfile')
#shutil.move('oldfile', 'newfile')

#import glob
#
#globs = glob.glob('*.py')
#print(globs)

import sys

#print(sys.argv)
#
#sys.stderr.write('oops\n')
##sys.exit()
#sys.stderr.write('err\n')

import re

#matches = re.findall(r'\w+', 'abc abc')
#print(matches)
#matches = re.sub(r'(\w+) \1', r'\1', 'abc abc')
#print(matches)
#
#print('tea for too'.replace('too', 'two'))

import random

#choice = random.choice(['apple', 'pear', 'banana', 'apple', 'pear', 'banana'])
#print(choice)
#
#sample = random.sample(range(100), 10)
#sample = random.sample(['apple', 'pear', 'banana', 'apple', 'pear', 'banana'], 2)
#print(sample)
#
#float = random.random()
#print(float)
#
#choice = random.choice(range(6))
#print(choice)
#
#random_range = random.randrange(6)
#print(random_range)

from urllib.request import urlopen

#with urlopen('http://pray.in.ua') as resp:
#    for line in resp:
#        line = line.decode('utf-8')
#        line = line.replace('\n', '')
#        print(line)
##        if 'EST' in line or 'EDT' in line:
##            print(line)

from datetime import date
#today = date.today()
##print(today)
##print(today.strftime('%Y--%m--%d %H::%M::%S %T %z'))
#
#birthday = date(1964, 7, 31)
#age = today - birthday
##print(age.days, 'days')
#print(age)

import zlib
#s = b'witch which has which witches wrist watch'
#print(len(s))
#t = zlib.compress(s)
#print(len(t))
#print(t)
#d = zlib.decompress(t)
#print(d)
#print(zlib.crc32(s))
#print(zlib.crc32(t))
#print(zlib.crc32(d))

from timeit import Timer
#print(Timer('t=a; a=b; b=a', 'a=1; b=2').timeit())
#print(Timer('a,b = b,a', 'a=1; b=2').timeit())

#def average(values):
#    """Computes the averages.
#
#    >>> print(average([20, 30, 70]))
#    40.0
#    """
#    return sum(values) / len(values)
#
import doctest
#doctest.testmod()

import unittest
#
#class TestStats(unittest.TestCase):
#    def test_average(self):
#        self.assertEqual(average([20, 30, 70]), 40.0)
#
#unittest.main()

import reprlib
#
#print(set('supercalifragilisticexpialidocious'))
#print(reprlib.repr(set('supercalifragilisticexpialidocious')))

import pprint
#
#t = [[2, 42, 'abcdefg', 'abcdefg'], 3, 'zbcxvzbc', [1, 2, 3, 4, 5]]
#pprint.pprint(t, width=40)

import textwrap
#
#doc = """The wrap() method is just like fill() except that it returns
#    a list of strings instead of one big string with newlines to separate
#    the wrapped lines."""
#print(textwrap.fill(doc, width=40))
#print(textwrap.wrap(doc, width=40))

from string import Template
#
#t = Template('${village}folk send $$10 to $cause')
#print(t.substitute(village='Nottingham', cause='the ditch fund'))
#print(t.safe_substitute(village='Nottingham'))

import struct
#
#with open('myfile.zip', 'rb') as f:
#    data = f.read()
#
#start = 0
## I = 4 bytes
## H = 2 bytes
## < = little-endian byte order
#fields = struct.unpack('<IIIHH', data[start:start+16)

import threading
#
#class Async(threading.Thread):
#
#    def __init__(self):
#        threading.Thread.__init__(self)
#
#    def run(self):
#        pass
#
#background = Async()
#background.start()
#
#print('The main program continues to run in foreground.')
#
#background.join() # Wait for the background task to finish
#
#print('Main program waited until background was done.')

import logging
#
#logging.debug('Debugging information')
#logging.info('Informational message')
#logging.warning('Warning:config file %s not found', 'server.conf')
#logging.error('Error occurred')
#logging.critical('Critical error -- shutting down')

from array import array
#
#a = array('H', [4000, 10, 700, 22222])
#print(sum(a))
#print(a[1:3])

from collections import deque
#
#d = deque(["task1", "task2", "task3"])
#d.append("task4")
#print(d)
#print(d.popleft())

import bisect
#
#scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
#bisect.insort(scores, (300, 'ruby'))
#print(scores)

from heapq import heapify, heappop, heappush
#
#data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
#heapify(data)
#print(data)
#heappush(data, -5)
#print([heappop(data) for i in range(3)])

from decimal import Decimal, getcontext
#
#print(round(Decimal('0.70') * Decimal('1.05'), 2))
#print(round(0.70 * 1.05, 2))
#
#print(Decimal('1.00') % Decimal('.10'))
#print(1.00 % .10)
#
#print( sum([Decimal('0.1')]*10) == Decimal('1.0') )
#print( sum([0.1]*10) == 1.0 )
#
#getcontext().prec = 36
#print(Decimal(1) / Decimal(7))

## reverse
#fruit = 'banana'
#index = 0
#while index < len(fruit):
#    zindex = len(fruit) - 1 - index
#    print(fruit[zindex], end='')
#    index += 1
#print()
#
#for char in fruit:
#    print(char, end='')
#print()

#prefixes = 'JKLMNOPQ'
#suffix = 'ack'
#
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
#        print(i, j)
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

    i = 0
    while i < len(word) - 1:
        if word[i] > word[i+1]:
            return False
        i += 1
    return True

from importlib import reload;
#import lru_cache;
#reload(lru_cache)

from datetime import datetime
#
#print(datetime.utcnow())

## FizzBuzz
#for i in range(1, 100):
#    if i % 3 == 0 and i % 5 == 0:
#        print('FizzBuzz', end=' ')
#    elif i % 3 == 0:
#        print('Fizz', end=' ')
#    elif i % 5 == 0:
#        print('Buzz', end=' ')
#    else:
#        print(i, end=' ')
#print()




