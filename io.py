# encoding=utf-8

def reverse(text):
    return text[::-1]

def normalize(text):
    norm = []
    for l in text:
        if str.isalpha(l):
            norm.append(l)
#    return str.lower(str.join('', norm))
    return ''.join(norm).lower()

def is_palindrome(text):
    return normalize(text) == reverse(normalize(text))

#something = input('Enter text: ')
something = "Rise to vote, sir."
if is_palindrome(something):
    print('Yes, it is a palindrome')
else:
    print('No, it is not a palindrome')



#poem = '''\
#Programming is fun
#When the work is done
#if you wanna make your work also fun:
#    use Python!
#'''
#
#f = open('poem.txt', 'w')
#f.write(poem)
#f.close()
#
#f = open('poem.txt')
#while True:
#    line = f.readline()
#    if len(line) == 0:
#        break
#    print(line, end='')
#f.close()


#import pickle
#
#shoplistfile = 'shoplist.data'
#
#shoplist = ['apple', 'mango', 'carrot']
#
#f = open(shoplistfile, 'wb')
#pickle.dump(shoplist, f)
#f.close()
#
#del shoplist
#
#f = open(shoplistfile, 'rb')
#storedlist = pickle.load(f)
#print(storedlist)



#import io
#
#f = io.open("abc.txt", "wt", encoding="utf-8")
#f.write(u"Non-English text here: Слава Богу")
#f.close()
#
#text = io.open("abc.txt", encoding="utf-8").read()
#print(text)
