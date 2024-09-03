N=int(input('Enter a number: '))
f= input('Enter filename: ')
f1=open(f,'r')
allline=f1.readlines()
f1.close()
for i in range(N):
    print(allline[i],end='')