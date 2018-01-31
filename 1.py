#!/usr/bin/env python3

print('{}' 'Py' 'thon')
print(
    'Put several strings within parentheses '
    'to have them joined together.'
)


a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

b = list(enumerate(a))
for elem in b:
    print(elem[0], elem[1])


def concat(*args, sep='/'):
#def concat(sep='/', *args):
    return sep.join(args)

print(concat('earth', 'mars', 'venus'))


print(list(range(3, 6)))
args = [3, 6]
print(list(range(*args)))

args = {'dog', 'cat'}
shmargs = (*args,)
print(shmargs)


pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key = lambda i: i[1])
print(pairs)


def doc_strings():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass

from collections import deque

q = deque(["Eric", "John", "Michael"])
q.append("Terry")
q.popleft()
print(q)

squares = []
x = 42
print(x)
for x in range(10):
    squares.append(x**2)
print(squares)
print(x)

x = 42
print(x)
squares = list(map(lambda x: x**2, range(10)))
print(squares)
print(x)

x = 42
print(x)
squares = [x**2 for x in range(10)]
print(squares)
squares = [x**2 for x in range(10) if x > 5]
print(squares)
print(x)

[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
#[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print(list(zip(*matrix)))

a = set('abracadabra')
b = set('alacazam')

#a
#{'a', 'r', 'b', 'c', 'd'}

#a - b
#{'r', 'd', 'b'}

#a | b
#{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}

#a & b
#{'a', 'c'}

#a ^ b
#{'r', 'd', 'b', 'm', 'z', 'l'}

a = {x for x in 'abracadabra' if x not in 'abc'}
#a
#{'r', 'd'}

d = {'q': 'w', 'a': 's', 'z': 'x'}
print(d.keys())
print(list(d.keys()))
print(sorted(d.keys()))

d = dict({1: 2})
print(d)

d = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(d)

d = dict((('sape', 4139), ('guido', 4127), ('jack', 4098)))
print(d)

d = {x: x**2 for x in range(6)}
print(d)

d = dict(sape = 4139, guido = 4127)
print(d)


knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

questions = ['name', 'quest', 'favourite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {}? It is {}'.format(q, a))

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

print('Українська' > 'Русский')
print('Українська' == 'Русский')
print('Українська' < 'Русский')

# '!a' apply ascii(), '!s' apply str(), '!r' apply repr()
contents = 'eels'
print('My hovercraft is full of {!r}.'.format(contents))

table = { 'k1': 11, 'k2': 22, 'k3': 33 }
print('K1: {0[k1]:d}; K2: {0[k2]:d}; K3: {0[k3]:d}'.format(table))
print('K1: {k1:d}; K2: {k2:d}; K3: {k3:d}'.format(**table))

with open('workfile') as f:
    read_data = f.read()
print(f.closed)

with open('poem.txt') as f:
    for line in f:
        print(line, end='')

with open('poem.txt') as f:
    lines1 = list(f)
    lines1 = lines1[::-1]
    print(lines1)
    print(f.tell())
    f.seek(0)
    lines2 = f.readlines()
#    lines = sorted(lines, reverse=True)
    lines2 = lines2[::-1]
    print(lines2)

with open('workfile', 'w') as f:
    value = ('the answer', 42)
    s = str(value)
    f.write(s)

import json

json1 = json.dumps( [1, 'simple', 'list'] )
print(json1)

with open('workfile', 'w') as f:
    json.dump(json1, f)
    f.write('\n')

with open('workfile') as f:
    x = json.load(f)
    print(x)

from random import randint

cons = ['b', 'd']
print(len(cons))
for i in range(0, 3):
    con = cons[randint(0, len(cons) - 1)]
    word = 'a' + con + 'i' + con + 'as'
    print(word)


class A:
    def m1(self):
        print('m1')

a = A()
a.m1()
#a.m1 = 42
#a.m1()


print([].__class__)
print('42'.__class__)
print(int(42).__class__)

print(a.m1.__self__)
print(a.m1.__func__)

data = ['a', 'b', 'c']
print(len(data))

for r in range(len(data), -1, -1):
    print(r)

table = {x: x*2 for x in range(1, 5)}
print(table)

import sys

sys.stderr.write('err\n')
#sys.exit()
sys.stderr.write('err\n')

import re

matches = re.findall(r'\w+', 'abc abc')
print(matches)
matches = re.sub(r'(\w+) \1', r'\1', 'abc abc')
print(matches)

print('tea for too'.replace('too', 'two'))

import random

choice = random.choice(['apple', 'pear', 'banana'])
print(choice)

sample = random.sample(range(100), 10)
print(sample)

float = random.random()
print(float)

random_range = random.randrange(6)
print(random_range)

from urllib.request import urlopen

#with urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl') as resp:
#    for line in resp:
#        line = line.decode('utf-8')
#        line = line.replace('\n', '')
#        if 'EST' in line or 'EDT' in line:
#            print(line)

from datetime import date
today = date.today()
print(today)
print(today.strftime('%Y--%m--%d %H::%M::%S'))

birthday = date(1964, 7, 31)
age = today - birthday
print(age.days, 'days')
print(age)

import zlib
s = b'witch which has which witches wrist watch'
print(len(s))
t = zlib.compress(s)
print(len(t))
print(t)
d = zlib.decompress(t)
print(d)
print(zlib.crc32(s))
print(zlib.crc32(t))
print(zlib.crc32(d))

from timeit import Timer
print(Timer('t=a; a=b; b=a', 'a=1; b=2').timeit())
print(Timer('a,b = b,a', 'a=1; b=2').timeit())

def average(values):
    """Computes the averages.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()

import unittest

class TestStats(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)

unittest.main()


