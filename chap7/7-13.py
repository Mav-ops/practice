import random
N=random.randint(1,10)
a=set()
b=set()
for i in range(N):
    n=random.randint(0,9)
    a.add(n)
print(a)

for j in range(N):
    n = random.randint(0, 9)
    b.add(n)
print(b)

print(a|b,a&b)
