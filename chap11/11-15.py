# -*- coding: utf-8 -*-

def f(n):
    #如当前n未到末尾则打印当前并从n+1位置再进行函数
    if n + 1< len(str):
        print (str[n])
        f(n+1)
    #已到达字符串末尾
    else:
        print (str[n])


if __name__ == '__main__':
    str = 'this is a string'
    f(0)