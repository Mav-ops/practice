def getfactors(num):
    alist = []
    a = num // 2
    while a >= 1:
        if num % a == 0:
            alist.append(a)
        a -= 1
    alist.sort()
    return alist

def isperfect(num):
    sum=0
    print(getfactors(num))
    for i in getfactors(num):
        sum+=i
    if sum==num:
        return 1
    else:
        return 0

print(isperfect(int(input('enter a number:'))))





