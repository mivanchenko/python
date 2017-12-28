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



