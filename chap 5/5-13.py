def Test(h,m):
    minute=h*60+m
    return minute

if __name__=='__main__':
    while True:
        h=int(input('hour:'))
        m=int(input('minute:'))
        if (h<23 and h>-1)and(m<60 and m>-1):
            print('the time is %d'%Test(h,m))
        else:
            print('please input correctly!')