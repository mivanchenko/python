
a = ['q', 'w', 0.0]

if not all(a): print('ok') 

print(format(14, '#b'))
print(format(14, 'b'))

bytes = bytearray([3,2,1])
print(bytes)
print(bytes[0])
bytes[1] = 4
print(bytes)

a = "abc"
a = a.replace("a", "f")
print(a)
a = b"abc"
a = a.replace(b"a", b"f")
print(a)

class Computer:
    monitor = 'LG'

print(Computer.monitor)
delattr(Computer, "monitor")
if not hasattr(Computer, "monitor"): print('ok')

a = 13
b = 4
print(a // b)
print(a % b)
print(divmod(a, b))

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
list_seasons = list(enumerate(seasons))
print(list_seasons)

dict_season = {}
for season in list_seasons:
    dict_season[season[0]] = season[1]
print(dict_season)

seasons = ['', 'Spring', 0, 'Summer', False, 'Fall', None, 'Winter']
f_seasons = filter(None, seasons)
for season in f_seasons:
    print(season)

def summer_only(arg):
    if arg == 'Summer': return True
    return False

f_seasons = filter(summer_only, seasons)
for season in f_seasons:
    print(season)

myset = {'jack', 'sjoerd'}
print(myset)
print('jack' in myset)

mydict = { 'name': 'jack' }
print(mydict)
mydict[frozenset(myset)] = 42
print(mydict)
print(len(mydict))

print(globals())

print(hash(frozenset(myset)))
print(hash(frozenset(myset)))
print(hash(f_seasons))
print(hash(f_seasons))
print(hash(42))
print(hash(42.0))
print(hash('42.0'))
print(hash('42.0'))

print(format(255, '#x'), format(255, 'x'), format(255, 'X'))


print(id(hash(42)))
print(id(hash(42.0)))

id42 = hash(42)
id420 = hash(42.0)
print(id(id42))
print(id(id420))

with open('poem.txt') as f:
    for line in iter(f.readline, '\n'):
        print(line, end='')

print(globals())
print(locals())

def add_one(arg):
    return arg + 1

print(map(add_one, (1, 2, 3)))
for i in map(add_one, (1, 2, 3)): print(i)

iter = map(add_one, (1, 2, 3))
a1 = next(iter)
a2 = next(iter)
a3 = next(iter)
print(a3, a2, a1)

a4 = object
print(a4)

a4 = object()
print(a4)

print(end=':')
print(end='\n')

class Parrot:
    def __init__(self):
        self._voltage = 100

#    @property
    def voltage(self):
        '''Get the current voltage.'''
        return self._voltage

    def voltage(self, voltage):
        '''Set the current voltage.'''
        self._voltage = voltage
        return voltage

parrot = Parrot()
#print(parrot.voltage())
#parrot.voltage(200)
#print(parrot.voltage())

class C:
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, val):
        self._x = val

    def delx(self):
        del self._x

    x = property(getx, setx, delx, "I'm the 'x' property.")

c = C()
c.setx(1)
print(c.x)
c.x = 2
print(c.x)
del c.x
#print(c.x)

class C:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value + 1

    @x.deleter
    def x(self):
        del self._x

c = C()
c.x = 3
print(c.x)
#c.x(4)

print(reversed('abc'))
print('abc'[::-1])
for i in reversed('abc'): print(i)
print(''.join(reversed('abc')))

print(round(0.5))
print(round(-0.5))
print(round(1.5))
print(round(1.55, 1))

s_list = sorted(['d', 'a', 't', 'a'], reverse = True)
print(s_list)
s_list = sorted({'d': 'b', 't': 'a'})
print(s_list)

#class C(B):
#    def method(self, arg):
#        super().method(arg)

d1 = dict(a = 1)
d2 = { 'a': 1 }
print(d1)
print(d2)

x = [1, 2, 3]
y = [4, 5, 6]
zipped = zip(x, y)
print(list(zipped))

#x2, y2 = zip(*zip(x, y))
x2, y2 = zip((1, 4),(2, 5),(3, 6))
print(list(x2), list(y2))

