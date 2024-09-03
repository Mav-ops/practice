import random
N=random.randint(1,10)
a=set()
b=set()
a1=set()
b1=set()
for i in range(N):
    n=random.randint(0,9)
    a.add(n)
print('A:',a)

for j in range(N):
    n = random.randint(0, 9)
    b.add(n)
print('B:',b)

i=0
while i<=3:
    asw1=map(int,input('A|B=').split(' '))
    asw2=map(int,input('A&B=').split(' '))
    for j in asw1:
        a1.add(j)
    print(a1)
    for k in asw2:
        b1.add(k)
    print(b1)
    if a1==a|b and b1==a&b:
        print("You are right!")
        break
    else:
        print('Error,try angin,you have %d remaining chances.'%(3-i))
        i+=1
        if i==4:
            print('answer is:',a | b, a & b)


#！！！！！！！！！！！处理不了空集