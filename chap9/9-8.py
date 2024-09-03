m=input('Enter a module name:')
module=__import__(m)
m1=dir(module)
print(m1)
for i in m1:
    print('name:',i)
    print('type:',type(getattr(module,i)))
    print('value:',getattr(module,i))
    print()