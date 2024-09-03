'''
num_str=input('enter a number:')
num_num=int(num_str)

fac_list=list(range(1,num_num+1))
print('BEFORE:',fac_list)

i=0
while i<len(fac_list):
    if num_num%fac_list[i]==0:
        del fac_list[i]            #### 2去不掉，WHY？？？

    i=i+1

print('AFTER',fac_list)
'''
num_str = input('Enter a number:')
num_num = int(num_str)
#把输入的数转换成整形数
fac_list = list(range(1,num_num+1))
#创建一个从1到num_num的列表
print('BEFORE: ',fac_list)
fac_list1 = []
i=0
while i < len(fac_list):
    if num_num % fac_list[i] == 0:
        #当数能够整除i时，将i存储到另一个列表中
        fac_list1.append(fac_list[i])
    i += 1
for j in fac_list1:
    fac_list.remove(j)
    #历遍可以整除数的列表，将这些数从初始列表中一一删除

print(fac_list)
