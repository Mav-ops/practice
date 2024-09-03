def getfactors(num):
    alist=[1]
    alist.append(num)
    a=num//2
    while a>1:
        if num%a==0:
            alist.append(a)
        a-=1
    alist.sort()
    return alist

print(getfactors(int(input('enter a number:'))))
