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

#try:
#    fin = open('bad_file.txt', 'w')
#    for line in fin:
#        print(line)
#    fin.close()
#except:
#    pass
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

#sed('old', 'new', 'input1.txt', 'output1.txt')

import pickle

#t1 = [1, 2, 3]
#t1_dump = pickle.dumps(t1)
#print(t1_dump)
#
#t2 = pickle.loads(t1_dump)
#print(t2)
#
#print(t1 == t2)
#print(t1 is t2)

import shelve

#t1 = [1, 2, 3]
#shelf = shelve.open('shelf.data', 'c')
#shelf['1'] = t1
#shelf.close()
#
#shelf = shelve.open('shelf.data')
#try:
#    print(shelf['1'])
#    print(shelf['2'])
#except:
#    print('No data')

#cmd = 'ls -l'
#fp = os.popen(cmd)
#res = fp.read()
#print(len(res))
#stat = fp.close()
#print(stat)

#filename = 'poem.txt'
#cmd = 'md5 ' + filename
#fp = os.popen(cmd)
#res = fp.read()
#stat = fp.close()
#print(res)

# find duplicates

#def get_paths_for(a_dirname, an_extension):
#    paths = []
#    path = os.path.abspath(a_dirname)
#    for dirpath, dirnames, filenames in os.walk(path):
#        if '.git' in dirnames:
#            dirnames.remove('.git')
#        for filename in filenames:
#            name, ext = os.path.splitext(filename)
#            if ext == an_extension:
#                paths.append(os.path.join(dirpath, filename))
#    return paths
#
#paths = get_paths_for('../../Music', '.mp3')
#print(len(paths))
#md5 = {}
#for path in paths:
#    cmd = 'md5 {!r}'.format(path)
#    fp = os.popen(cmd)
#    res = fp.read()
#    stat = fp.close()
#    if stat is not None:
#        print('Something went wrong with', path)
#    res = res.rstrip().split()[-1]
#    if res in md5:
#        print(path, 'is a duplicate of', md5[res])
#    else:
#        md5[res] = path
#print(len(md5.items()))


