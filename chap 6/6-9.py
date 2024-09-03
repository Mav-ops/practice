def hour(minu):
    m=int(minu)
    a=m//60
    b=m%60
    return (a,b)

minu=input("ENnter minutes:")
print('%d hours %d minutes.'%(hour(minu)))

'''

def time(mins):
    hour = mins // 60
    minute = mins % 60
    return '%d:%d' % (hour, minute)


if __name__ == '__main__':
    minutes = int(input("Minutes: "))
    print(time(minutes))

'''