import math

def safe_sqrt(num):
    try:
        num=math.sqrt(num)
        return num
    except ValueError:
        num=-1*num
        num=math.sqrt(num)
        n='%fi'%num
        return n

if __name__=='__main__':
    print(safe_sqrt(float(input('enter a number:'))))