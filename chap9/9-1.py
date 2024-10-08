import os
ls=os.linesep
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

f=open(fname,'r')
for eachline in f:
    if eachline[0]=='#':
        continue
    elif '#' in eachline:
        loc=eachline.find('#')
        print(eachline[:loc])
    else:
        print(eachline)