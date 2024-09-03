dict1={}
dict2={}
i = 1
while True:
    key=input('key%d:'%i)
    value=input('value%d:'%i)
    if key in dict1.keys():
        print('error,the dict1 has the key!')
    if value in dict1.values():
        print('error,the dict1 has the value!')
    else:
        dict1[key]=value
        i+=1
    print('continue to add item to the dict1? ')
    a=input('Y/N')
    if a in 'Yy':
        continue
    else:
        break

print(dict1)

for i in dict1.keys():
    dict2[dict1[i]]=i
print(dict2)

'''
dict_sort = {1: 'a', 2: 'b'}
dictreverse = {}
for key, value in dict_sort.items():
    dictreverse[value] = key
print(dictreverse)
'''