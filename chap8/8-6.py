def isprime(num):
    a=num//2
    while a>1:
        if num%a==0:
            return False
        a-=1
    else:
        return True

def getfactorsDepart(num):
    alist=[]
    a=num//2
    while a>1:
        if num%a==0:
            if isprime(a):
                alist.append(a)
                num = int(num/a)
                getfactorsDepart(num)
            else:
                a-=1
        else:
            a-=1
    alist.sort()
    return alist

print(getfactorsDepart(int(input('enter a number:'))))
