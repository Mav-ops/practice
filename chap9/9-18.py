num=int(input('Enter a number between 0~255:'))
filename=input('Enter filename:')
ch=chr(num)
numcount=0
f=open(filename,'r')
for line in f:
    numcount+=line.count(ch)

print(numcount)