#print("Hello, world", end=';')
#print('{0:.3f}'.format(1.0/3))
#print('{0:_^11}'.format('hello'))
#print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))
#
#age = 20
#name = 'Swaroop'
#print('{0} was {1} years old when he wrote this book'.format(name, age))
#print('{} was {} years old when he wrote this book'.format(name, age))
#
#print('This is the first line\nThis is the second line')
#print(r"Newlines are indicated by \n")
#
#s = '''This is a multi-line string.
#This is the second line.'''
#print(s)
#
#print('Perimeter is', 2)
#
#
#number = 23
##guess = int(input('Your guess:'))
#guess = 23
#if guess == number:
#   # new block
#   print('Congrats!')
#elif guess < number:
#   # no
#   print('elif')
#else:
#   # no
#   print('else')
#
#print('done')
#
#
#running = False
#while running:
#   guess = int(input('Enter an integer : '))
#else:
#   print('The while loop is over.')
#
#
#for i in range(1, 5):
#    print(i)
#else:
#    print('The for loop is over')
#
#
#for i in list(range(5)):
#    print(i)
#else:
#    print('The for loop is over')
#
#
#for i in list(range(1, 5, 2)):
#    print(i)
#else:
#    print('The for loop is over')
#
#
#while True:
##    s = input('Enter something:')
#    s = 'quit'
#    if s == 'quit':
#        break
#    print('Length of the string is', len(s))
#print('Done')
#
#
#while False:
#    s = input('Enter something : ')
#    if s == 'quit':
#        break
#    if len(s) < 3:
#        print('Too small')
#        continue
#    print('Input is of sufficient length')
#
#def print_max(a, b):
#    if a > b:
#        print(a, 'is maximum')
#    elif a == b:
#        print(a, 'is equal to', b)
#    else:
#        print(b, 'is maximum')
#
#print_max(3, 4)
#
#x = 5
#y = 7
#print_max(x, y)
#
#x = 50
#
#def func():
#    print('y is', y)
#    global x
#    print('x is', x)
#    x = 2
#    print('x is', x)
#
#func()
#
#def say(message, times=1):
#    print(message * times)
#
#say('Hello')
#say('World', 5)
#
#def func(a, b=5, c=10):
#    print('a: {} b: {} c: {}'.format(a, b, c))
#
#func( 1, c = 42 )
#func( c = 42, a = 100 )
#
#def total(a=5, *numbers, **phonebook):
#    print('a', a)
#
#    for single_item in numbers:
#        print('single_item', single_item)
#
#    for first_part, second_part in phonebook.items():
#        print(first_part, second_part)
#    return 1
#
#print( total( 10, 1, 2, 3, Jack = 1123, John = 2231, Inge = 1560 ) )
#
#def print_max(x, y):
#    '''
#    Prints the maximum of two numbers.
#
#    The two values must be integers.
#    '''
#    # convert to integers, if possible
#    x = int(x)
#    y = int(y)
#
#    if x > y:
#        print(x, 'is maximum')
#    else:
#        print(y, 'is maximum')
#
#print_max(3, 5)
##print( print_max.__doc__ )
#help(print_max)
#
#import sys
#import os
#from math import sqrt
#
#print('The command line arguments are:')
#for i in sys.argv:
#    print(i)
#print('\n\nThe Python path is', sys.path, '\n')
#print(os.getcwd())
#print('Sq root of 16 is', sqrt(16))
#
#if __name__ == '__main__':
#    print('This program is being run by itself')
#else:
#    print('I am being imported from another module')

def hi():
    print('Hello, my module is speaking')

__version__ = '0.1'











