import sys

file1=sys.argv[1]
file2=sys.argv[2]

f1=open(file1,'r')
f2=open(file2,'a+')
f2.write('\n')
for line in f1:
    f2.write(line)
f1.close()
f2.close()