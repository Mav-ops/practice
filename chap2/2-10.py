while True:
    print('input a number 1~100:')
    a=int(input())
    if a<=100 and a>=1:
        print(a)
        break
    else:
        print('error,input again')