#!/usr/bin/env python3

#try:
#    text = input('Enter something: ')
#except EOFError:
#    print('Why did you do an EOF on me?')
#except KeyboardInterrupt:
#    print('You cancelled the operation.')
#else:
#    print('You entered {}'.format(text))


#try:
#    text = input('Enter something: ')
#except (EOFError, KeyboardInterrupt):
#    print('Why did you do an EOF on me?')
#    print('You cancelled the operation.')
#else:
#    print('You entered {}'.format(text))


#try:
#    text = input('Enter something: ')
#except:
#    print('Something has happened')
#else:
#    print('You entered {}'.format(text))


#class ShortInputException(Exception):
#    '''A user-defined exception class.'''
#    def __init__(self, length, atleast):
#        Exception.__init__(self)
#        self.length = length
#        self.atleast = atleast
#
#try:
#    text = input('Enter something: ')
#    if len(text) < 3:
#        raise ShortInputException(len(text), 3)
#    # ...
#except EOFError:
#    print('Why did you do an EOF on me?')
#except ShortInputException as ex:
#    print((
#        'ShortInputException: The input was: '
#        + '{0} long, expected at least {1}'
#    ).format(ex.length, ex.atleast))
#else:
#    print('No exception was raised.')


#import sys
#import time
#
##f = None
#try:
##    f.open('poem.txt')
#    f = open('poem.txt')
#    while True:
#        line = f.readline()
#        if len(line) == 0:
#            break
#        print(line, end='')
#        sys.stdout.flush()
#        print('Press ctrl+c now')
#        time.sleep(2)
#except IOError:
#    print('Could not find file poem.txt')
#except KeyboardInterrupt:
#    print('!! You cancelled the reading from the file.')
#finally:
#    if f:
#        f.close()
#    print('(Cleaning up: closed the file)')
#import time
#
##f = None
#try:
##    f.open('poem.txt')
#    f = open('poem.txt')
#    while True:
#        line = f.readline()
#        if len(line) == 0:
#            break
#        print(line, end='')
#        sys.stdout.flush()
#        print('Press ctrl+c now')
#        time.sleep(2)
#except IOError:
#    print('Could not find file poem.txt')
#except KeyboardInterrupt:
#    print('!! You cancelled the reading from the file.')
#finally:
#    if f:
#        f.close()
#    print('(Cleaning up: closed the file)')
#
#
#import sys
#import time
#
#with open('poem.txt') as f:
#    for line in f:
#        if len(line) == 0:
#            break
#        print(line, end='')
#        sys.stdout.flush()
#        print('Press ctrl+c now')
#        time.sleep(2)

class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
        print('raise')
    except D:
        print('D')
    except C:
        print('C')
    except B:
        print('B')
    else:
        print('else')
    print('done')


try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))
    print(inst.args)
    print(inst)
    x, y = inst.args
    print('x =', x, 'y =', y)
