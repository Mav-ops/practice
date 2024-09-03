v=[]
for x in range(21):
    if x%2==0:
        v.append(int(x))
print(v)

def judge(a,b):
    if a<b:
        a,b=b,a
    if a%b==0:
        return True
    else:
        return False

a=int(input('enter a:'))
b=int(input('enter b:'))
r=judge(a,b)
print(r)