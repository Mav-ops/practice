'''  矩阵加法

m = int(input('矩阵行数')) # 矩阵行数
n = int(input('矩阵列数')) # 矩阵列数
a = []
b = []
c = []
for i in range(m):
    a.append(list(map(int, input('输入矩阵A的第%d行'%(i+1)).split())))
for i in range(m):
    b.append(list(map(int, input('输入矩阵B的第%d行'%(i+1)).split())))
for i in range(m):
    t = []
    for j in range(n):
        t.append(a[i][j] + b[i][j])
    c.append(t)
for i in c:
    for j in i:
        print(j, end=' ')
    print()

'''
#map(int,input().split())
# 将输入的值(input.split（）的东西也叫做可迭代对象)通过空格分开，
# int函数将其转化为整型数据，map（）函数将输入的多个数据的结果生成一个迭代器a，
# 迭代器顾名思义就是可迭代的对象经过对应的函数处理之后得到的结果封装在a里面



#     矩阵乘法
#m*n  n*p   m*p
m=input('输入矩阵A的行数：')
n=input('输入矩阵A的列数：')
q=input('输入矩阵B的行数：')
p=input('输入矩阵B的列数：')
if n!=q:
    print('ERROR,矩阵A和B无法相乘')

a = []
b = []
c = []
for i in range(int(m)):
    a.append(list(map(int, input('输入矩阵A的第%d行'%(i+1)).split())))
for i in range(int(n)):
    b.append(list(map(int, input('输入矩阵B的第%d行'%(i+1)).split())))
for i in range(int(m)):
    c.append([0] * int(p))  # 存放乘法结果的矩阵中所有初始值为0
                                 # c是m行p列矩阵
for i in range(int(m)):
    for j in range(int(p)):          #结果是 m*p
        for k in range(int(n)):              #循环，range(n)
            c[i][j] += a[i][k] * b[k][j]

for i in c:
    for j in i:
        print(j, end=' ')
    print()