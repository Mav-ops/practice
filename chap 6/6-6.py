str = input('Str: ')

length = len(str)
print('原始长度为%d'%length)
for i in range(0, length):
    if str[i] != ' ':
        str = str[i:]
        print('去掉前空格长度为%d'%len(str))
        break
    else:     #str[i]==' ',跳过
        pass

for i in range(1, length + 1):
    if str[-1] != ' ':
        str = str[:]
        print('后面无空格，长度为%d'%len(str))
        break
    elif str[-i] != ' ':
        str = str[:-i + 1]
        print('去掉后面空格长度为%d'%len(str))
        break
    else:      #str[-i]==' ',跳过
        pass

print(str)