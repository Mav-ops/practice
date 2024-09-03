def grade(a):
    if a>100 or a<0:
        return ('error.')
    elif 90<=a:
        return ('A')
    elif 80<=a:
        return ('B')
    elif 70<=a:
        return ('C')
    elif 60<=a:
        return ('D')
    else:
        return ('F')

while True:
    a=int(input('grade:'))
    if a==0:
        break
    else:
        print(grade(a))