a=int(input('Enter total number of names:'))
i=0
n=0
namelist=[]
while i<a:
    str=input('Please enter name %d:'%(i+1))
    if len(str.split(','))!=2:
        n+=1
        print('Wrong format...should be Last,First.')
        print('You have done this %d time(s) already.Fixing input...'%n)
    else:
        namelist.append(str)
        i+=1

namelist.sort()
print('The sorted list (by last name) is')
for i in namelist:
    print(i.ljust(10,' '))