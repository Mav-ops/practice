print('Enter five number:')
v=[]
i=0
s=0
while i<5:
    a=input('n%d='%(i+1))
    v.extend([int(a)])
    s=s+v[i]
    i+=1
print(v)
print('sum=%d'%s)

print('Enter five number:')
v=[]
s=0
for i in range(5):
    a=input('n%d='%(i+1))
    v.extend([int(a)])
    s=s+v[i]
print(v)
print('sum=%d'%s)