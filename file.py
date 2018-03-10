#!/usr/bin/env python

#fout = open('output.txt', 'w')
#line1 = "This is it\n"
#fout.write(line1)
#line2 = "This is it again\n"
#fout.write(line2)
#x = 52
#fout.write(str(x))
#fout.write('\n')
#fout.close()

import os
cwd = os.getcwd()
#print(cwd)
#print(os.path.abspath('output.txt'))
#print(os.path.exists('output.txt'))
#print(os.path.isdir('output.txt'))
#print(os.path.isfile('output.txt'))
#print(os.listdir(cwd))

def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        if os.path.isfile(path):
            print(path)
        else:
            walk(path)

#walk(cwd)

for dirpath, dirnames, filenames in os.walk(cwd):
#    print(dirpath, dirnames, filenames)
    if '.git' in dirnames:
        dirnames.remove('.git')

try:
    fin = open('bad_file.txt', 'w')
    for line in fin:
        print(line)
    fin.close()
except:
    pass
#    print('Something went wrong')

def sed(pattern, replacement, filename1, filename2):
    try:
        fin = open(filename1)
    except:
        print('Failed to open', filename1)
        return

    try:
        fout = open(filename2, 'w')
    except:
        print('Failed to open', filename2)
        return

    for line in fin:
        line = line.replace(pattern, replacement)
        fout.write(line)

    fin.close()
    fout.close()
    return

sed('old', 'new', 'input1.txt', 'output1.txt')
