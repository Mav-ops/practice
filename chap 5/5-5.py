def coin(a):
    if a>100 or a<0:
        print('error')
    else:
        q=a//25
        d=(a-q*25)//10
        f=(a-q*25-d*10)//5
        c=a-q*25-d*10-f*5
        print('it can transfer'
              '%d quarters,%d dimes,%d nickels,%d cents'
              ''%(q,d,f,c))

while True:
    a=int(input('enter money:'))
    if a==0:
        break
    else:
        coin(a)