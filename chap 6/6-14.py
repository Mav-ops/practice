import random
import time
import sys

while 1:
    print('欢迎来到猜拳游戏! 当前时间是:', end='')
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    pw = input('请输入密码登录:')
    if pw.isdigit() and len(pw) == 11 and pw[0] == '1' and pw[1] in '3458':
        print('欢迎登录，可以进行猜拳了')
        print('=================================')
        break
    else:
        print('你的密码有误，请重新输入!')
        continue
while 1:
    arr = input('请进行猜拳(0退出游戏):')
    if arr == '0':
        sys.exit()
    else:
        if arr == '石头' or arr == '剪刀' or arr == '布':
            print('出招正确')
        else:
            print('出招错误，请重新出招:')
            continue
    brr = random.choice(['剪刀', '石头', '布'])
    if arr == '石头' and brr == '剪刀' or arr == '剪刀' and brr == '布' or arr == '布' and brr == '石头':
        print(f'你赢了，电脑出的是{brr}')
    elif arr == brr:
        print('平局')
    else:
        print(f'你输了，电脑出的是{brr}')