def isprime(num):
    a=num//2
    while a>1:
        if num%a==0:
            return False
        a-=1
    else:
        return True


print(isprime(int(input('enter a number:'))))

