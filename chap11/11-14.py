# -*- coding: utf-8 -*-
def f(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return f(n-1)+f(n-2)

if __name__ == '__main__':
    print (f(5))