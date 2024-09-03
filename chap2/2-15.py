#使用列表
a=int(input('n1='))
b=int(input('n2='))
c=int(input('n3='))
n=[]
if a>b:
    a,b=b,a
if a>c:
    a,c=c,a
if b>c:
    b,c=c,b
n.extend([a,b,c])
print(n)

#不使用列表
temp=0
if a<b:
    if b<c:
        print(a,b,c)
    else:
        if a<c:
            b,c=c,b
            print(a,b,c)
        if a>c:
            a,b,c=c,a,b
            print(a,b,c)
else:
    if b>c:
        a,c=c,a
        print(a,b,c)
    if c>a:
        a,b,c=b,a,c
        print(a,b,c)