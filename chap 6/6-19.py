num=int(input('输入数据个数：'))
row=int(input('输入列数：'))
s=input('选择 水平排序（s） 或 垂直排序(c)：')
a=[]
for i in range(num):
    a.append(input('输入第%d个数据：'%(i+1)))

if s=='s':
    q=num//row
    for i in range(row-1):
        for j in a[i*q:(i+1)*q]:
            print(j,end=' ')
        print('\n')
    for j in a[(row-1)*q:num]:
        print(j,end=' ')
if s=='c':
    q=num//row
