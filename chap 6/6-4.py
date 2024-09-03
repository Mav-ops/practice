num1=[]
while True:
    num=int(input('your grade:'))
    if num == 0:
        break
    if num>100 or num<0:
        print('error,input the right grade!')
    else:
        num1.append(num)

sum=0
for i in num1:
    sum+=int(i)
avg=sum/len(num1)
print(avg)


