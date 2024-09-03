def year(a):
    if a%100==0:
        if a%400==0:
            return ('is a leap year')
        else:
            return ('not a leap year')
    elif a%4==0:
        return ('is a leap year')
    else:
        return ('not a leap year')

while True:
    a=int(input('enter a year:'))
    if a==0:
        break
    else:
        print(year(a))