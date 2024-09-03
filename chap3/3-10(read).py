'readTextFile.py----read and display text file'

fname=input('enter filename:')
print()

#attemp to open file for reading

try:
    fobj=open(fname,'r')
except IOError:
    print('***file open error***')
else:
    #display contents to the screen
    for eachline in fobj:
        print(eachline,end=' ')
    fobj.close()

'''
另一种处理异常的方法
if os.path.exists(fname):
    fobj=open(fname,'r')
    for eachline in fobs:
        print(eachline,end=' ')
    fobj.close()
else:
    print('***file open error***')
'''