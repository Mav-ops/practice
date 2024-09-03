'makeTextFile.py----create text file'

import os
ls=os.linesep
###os.linesep字符串给出当前平台使用的行终止符。
###例如，Windows使用’\r\n’，Linux使用’\n’而Mac使用’\r’。

while True:
    fname=input('create a filename:')
    if os.path.exists(fname):
        print('ERROR:%s already exists'%fname)
    else:
        break

#get file content(text) lines
all=[]
print('\nEnter lines("."by itself to quit).\n')

#loop until user terminates input
while True:
    entry=input('>')
    if entry=='.':
        break
    else:
        all.append(entry)

#write lines to file with proper line-ending
fobj=open(fname,'w')
fobj.writelines(['%s%s'%(x,ls) for x in all])
fobj.close()
print('DONE!')


'''
另一种处理异常的方法
while True:
    fname=input('create a filename:')
    try:
       fff=open(fname,'r')        试图打开fname的文件
    expect IOError:               如果打不开说fname名字的文件未被建立，可以使用该名
        break
    else:                         如果打开说明已存在，报错，无法新建名为fname的文件
        print("ERROR:%s already exists'%fname")
'''