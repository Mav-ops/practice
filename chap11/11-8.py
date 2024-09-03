def year(a):
    if a%100==0:
        if a%400==0:
            return True
        else:
            return False
    elif a%4==0:
        return True
    else:
        return False

li=[1999,2000,2001,2002,2003,2004,2100,2400]
leapyear=[]
leapyear.extend(filter(year,li))
print(leapyear)

#列表解析
print([n for n in li if year(n)])