f=input('Enter filename: ')
f1=open(f,'r')
allline=f1.readlines()
f1.close()
sum=0
for i in allline:
    print(i,end='')
    sum+=1
    if sum==25:
        a=input('press any key to continue: ')
        sum=0