while True:
    s=0
    c=int(input('1 for sum,2 for ave,0 for exit:\n'))
    if c==1:
        for i in range(5):
            n=int(input('n%d='%(i+1)))
            s+=n
        print(s)

    if c==2:
        for i in range(5):
            n=int(input('n%d='%(i+1)))
            s+=n
        print(float(s/5))

    if c==0:
        break