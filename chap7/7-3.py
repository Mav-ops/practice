dict1={'d':100,'e':101,'a':97,'b':98,'c':99,'f':102}
print(dict1.keys())
print(sorted(dict1.keys()))
a=sorted(dict1.keys())
for v in a:
    print('key is %s,value is %d'%(v,dict1[v]))
print('\n')
def get_key_by_value(dictionary, value, default=None):
    for key, val in dictionary.items():
        if val == value:
            return key
    return default

b=sorted(dict1.values())
for i in b:
    print('value is %d,key is %s'%(i,get_key_by_value(dict1,i)))