
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
