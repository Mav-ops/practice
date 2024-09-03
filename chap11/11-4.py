def Test(m):
    hour=m//60
    minute=m-60*hour
    return (hour,minute)

if __name__=='__main__':
    while True:
        m=int(input('minute:'))
        print('the time is %d hours %d minutes'%Test(m))
