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


