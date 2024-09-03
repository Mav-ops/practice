def fanzhuan():
    xiaoxie = 'qwertyuiopasdfghjklzxcvbnm'
    daxie = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    str1 = input('please input your string')
    x = len(str1)
    str2 = []
    str3 = ""
    for i in range(x):
        #对输入字符串中的字符进行反转小大写操作，并且把转换完成的字符存储到另一个列表中
        if str1[i] in xiaoxie:
            str2.append(str1[i].upper()) ##upper() lower()是对字符串使用的，不是列表
        elif str1[i] in daxie:
            str2.append(str1[i].lower())
        else:
            str2.append(str1[i])
            #如果输入的不是字母，那就直接存储
    for j in str2:
        #将转换完的字符进行相加整合成一个新的字符串
        str3 += str(j)
    print(str3)

fanzhuan()


'''

def swapcase(str):
    return str.swapcase()

if __name__ == '__main__':
    str = input("Str: ")
    print(swapcase(str))

'''