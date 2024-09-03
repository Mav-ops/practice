def MaxMin(a,b):
    if a<b:
        a,b=b,a
    max=1;min=0
    for x in range(1,b+1):
        if a%x==0:
            max=x
    if max != 1:
        min = a * b / max
        print('最大公因数是%d' % max)
        print('最小公倍数是%d' % min)
    else:
        print('互素')
        print('最小公倍数是%d' % (a * b))

if __name__=='__main__':
    a=int(input('a:'))
    b=int(input('b:'))
    MaxMin(a,b)