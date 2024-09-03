dict1={}
while True:
    name=input('input employees name:')
    num=input('input employees number:')
    if num in dict1.keys():
        print('error,exist this number.')
    else:
        dict1[num]=name
    a=input('continue to add employees? Y/N')
    if a in 'Yy':
        continue
    else:
        break

def get_key_by_value(dic,value):
    for key,val in dic.items():
        if val==value:
            return key


#print('num:',sorted(dict1.keys()),'name:',dict1.values())
for i in sorted(dict1.keys()):
    print('num:',i.ljust(10,' '), 'name:',dict1[i].ljust(10,' '))

print('-'*20)
for j in sorted(dict1.values()):
    print('name:',j.ljust(10,' '),'num:',get_key_by_value(dict1,j).ljust(10,' '))