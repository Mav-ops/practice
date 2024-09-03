file=open('lupin','r')
list1=[]
for line in file:
    symbol=True
    while symbol:
        if len(line)<=80:
            list1.append(line)
            symbol=False
        else:
            count=int(len(line)/80)
            for i in range(count):
                j=79
                while line[j]!=' ':
                    j-=1
                list1.append(line[:j])
                line=line[j:]
print(list1)
file1=open('test2.txt','a')
for i in list1:
    file1.write(i)
    file1.write('\n')
f=open('test2.txt','r')
for j in f:
    print(j,len(j))

file1.close()