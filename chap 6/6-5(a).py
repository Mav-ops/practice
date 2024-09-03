x=input('input a string:')
i=0
print('The first symbol of the string is %s'%x[i])
while i>=0 and i<=len(x):
    c=input('"-" :back,"+":forward,"0":quit choose your option:')
    if c=='-':
        i-=1
        print(x[i])
    if c=='+':
        i+=1
        print(x[i])
    if c=='0':
        break
if c!='0':
    print('Error,out of range!')