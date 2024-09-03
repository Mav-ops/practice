from functools import reduce
import time


def mult(x,y):
    return x*y

def jiecheng(n):
    if n==0 or n==1:
        return 1
    else:
        return reduce(lambda x,y:x*y,range(1,n+1)) #reduce(mult,range(1,n+1))

print(jiecheng(5))

def digui(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*digui(n-1)

print(digui(5))


def testit(func,*arg):
    t0 = time.perf_counter()
    re = func(*arg)
    t1 = time.perf_counter()-t0
    return re,t1

if __name__=='__main__':
    re=testit(reduce,mult,range(1,6))
    re1=testit(reduce,lambda x,y:x*y,range(1,6))
    re2=testit(digui,5)

    print(re)
    print(re1)
    print(re2)