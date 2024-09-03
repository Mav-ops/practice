'''
str=input('enter a string of number:')
alist=list(str)
alist.sort()
alist.reverse()
print(alist)                     '''
num = input('your number')
num1 = []
num2 = []
for i in num:
    num1.append(int(i))
    #num1内存储的是数字大小
    num2.append(i)
    #num2内存储的是字符
num1.sort()
num1.reverse()
num2.sort()
num2.reverse()
print(num1)
print(num2)
