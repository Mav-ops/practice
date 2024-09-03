import random

def abc(num,count,len):
    l=[]
    n=len-count
    for i in range(n):
        randomnum=random.randint(0,255)
        symbol=True
        while symbol:
            if randomnum==num:
                randomnum=random.randint(0,255)
            else:
                l.append(randomnum)
                symbol=False

    for i in range(count):
        l.append(num)
    random.shuffle(l)
    print(l)
    f=open('test.txt','w')
    f.close()
    for i in l:
        f=open('test.txt','a')
        f.write('%08d   %d'%(int(bin(i)[2:]),i))
        f.write('\n')
        f.close()
        print('%08d   %d'%(int(bin(i)[2:]),i))

abc(66,5,20)