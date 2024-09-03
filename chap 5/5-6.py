while True:
    s=input('请输入要计算的式子：')
    if s==0:
        break
    else:
        if s.find('*')!=-1:
            ls=s.split('*')
            print(float(ls[0])*float(ls[1]))
        elif s.find('+')!=-1:
            ls=s.split('+')
            print(float(ls[0])+float(ls[1]))
