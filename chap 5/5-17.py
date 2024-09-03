import random
N=random.randint(1,100)
list1=[]
for i in range(N):
    n=random.randint(0,(2**31-1))
    list1.append(n)
list1.sort()

count=0
for i in list1:
    print(i,end=',')
    count+=1
    if count%10==0:
        print('\n')