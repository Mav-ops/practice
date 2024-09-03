def findchr(string, char):
    x = 0
    for i in range(len(string)):
        # 历遍字符串，如果字符等于所寻字符，那边把索引打印出来
        if string[i] == char:
            print(i,end=',')
            x += 1
    if x == 0:
        print('-1')


def rfindchr(string, char):
    for i in range(len(string) - 1, -1, -1):
        if string[i] == char:
            return i
    return -1


def subchr(string, origchar, newchar):
    stringlist = list(string)
    for i in range(len(string)):
        if stringlist[i] == origchar:
            stringlist[i] = newchar
    return ''.join(stringlist)



if __name__ == '__main__':
    string = input("String: ")
    char = input("Char: ")
    findchr(string, char)
    print('\n',rfindchr(string, char))
    newchar = input("Newchar: ")
    print(subchr(string, char, newchar))