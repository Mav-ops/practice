# -*- coding: utf-8 -*-
def max2(num,num2):
    if num >= num2:
        return num
    else:
        return num2

def min2(num,num2):
    if num <= num2:
        return num
    else:
        return num2

def my_max(lis,*therest):
    #判断传入的参数1是不是list，按list比较
    if isinstance(lis,list):
        temp = lis[0]
        for i in lis:
            if temp < i:
                temp = i
        return temp
    #传入的是参数集合，按参数集合比较
    else:
        temp = lis
        for i in therest:
            if temp < i:
                temp = i
        return temp


def my_min(lis,*therest):
    if isinstance(lis,list):
        temp = lis[0]
        for i in lis:
            if temp > i:
                temp = i
        return temp
    else:
        temp = lis
        for i in therest:
            if temp > i:
                temp = i
        return temp

if __name__ == '__main__':
    print (my_max([1,3,4,5]))
    print (my_min([2,4,1,7]))
    print (my_max(['wqe','rd','wes']))
    print (my_max(1,3,4,2))