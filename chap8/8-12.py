def out():
    '''8-12 输入整数1，整数2，显示一张表格，包括十进制，二进制，八进制，十六进制和ASCII'''
    # ASCII中 0-32 127 这34个是控制符，不用输出
    # 超过127的数字也不用输出，因为没有对应的ASCII
    num1 = int(input('Enter begin value:').strip())
    num2 = int(input('Enter end value:').strip())
    # 这里的dl,bl,ol,hl,al表示每一列的宽度
    dl,bl,ol,hl,al = \
    len(str(num2))+5,len(bin(num2))+3,len(oct(num2))+4,len(hex(num2))+3,5
    # 输出标题，居中
    print ('DEC'.center(dl),'BIN'.center(bl),'OCT'.center(ol),'HEX'.center(hl),'ASCII'.center(al))
    # 输出横线
    print ('-'*(sum([dl,bl,ol,hl,al])+5))
    ascii = ''
    for i in range(num1,num2+1):
        # Ascii 只有在这个区间内才显示
        if 32<i<127:ascii = chr(i)
        print(str(i).center(dl),bin(i)[2:].center(bl),oct(i)[1:].center(ol),hex(i)[2:].center(hl),ascii.center(al))
        ascii=''

out()