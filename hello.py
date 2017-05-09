print("Hello, world", end=';')
print('{0:.3f}'.format(1.0/3))
print('{0:_^11}'.format('hello'))
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))

age = 20
name = 'Swaroop'
print('{0} was {1} years old when he wrote this book'.format(name, age))
print('{} was {} years old when he wrote this book'.format(name, age))

print('This is the first line\nThis is the second line')
print(r"Newlines are indicated by \n")

s = '''This is a multi-line string.
This is the second line.'''
print(s)

print('Perimeter is', 2)


number = 23
#guess = int(input('Your guess:'))
guess = 23
if guess == number:
   # new block
   print('Congrats!')
elif guess < number:
   # no
   print('elif')
else:
   # no
   print('else')

print('done')


running = False
while running:
   guess = int(input('Enter an integer : '))
else:
   print('The while loop is over.')


for i in range(1, 5):
    print(i)
else:
    print('The for loop is over')


for i in list(range(5)):
    print(i)
else:
    print('The for loop is over')


for i in list(range(1, 5, 2)):
    print(i)
else:
    print('The for loop is over')


while True:
#    s = input('Enter something:')
    s = 'quit'
    if s == 'quit':
        break
    print('Length of the string is', len(s))
print('Done')


while True:
    s = input('Enter something : ')
    if s == 'quit':
        break
    if len(s) < 3:
        print('Too small')
        continue
    print('Input is of sufficient length')











