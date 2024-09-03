list = [1,1,2,3,6,74]
for i in list:
    if list.count(i) > 1:
        print(str(i)+'出现多次')
    else:
        print(str(i)+'没有重复出现')