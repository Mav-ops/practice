'read&writeTextFile.py'

import os
ls=os.linesep
def write():
    while True:
        fname = input('create a filename:')
        if os.path.exists(fname):
            print('ERROR:%s already exists' % fname)
        else:
            break

    # get file content(text) lines
    all = []
    print('\nEnter lines("."by itself to quit).\n')

    # loop until user terminates input
    while True:
        entry = input('>')
        if entry == '.':
            break
        else:
            all.append(entry)

    # write lines to file with proper line-ending
    fobj = open(fname, 'w')
    fobj.writelines(['%s%s' % (x, ls) for x in all])
    fobj.close()
    print('DONE!')


def read():
    fname = input('enter filename:')
    print()

    # attemp to open file for reading

    try:
        fobj = open(fname, 'r')
    except IOError:
        print('***file open error***')
    else:
        # display contents to the screen
        for eachline in fobj:
            print(eachline, end=' ')
        fobj.close()

i=0
while i!='q':
    i=input('"w" write,"r" read,"q" quit:')
    if i=='w':
        write()
    if i=='r':
        read()