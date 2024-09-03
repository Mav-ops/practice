str1=input('input the first string:')
str2=input('input the second string:')
if len(str1)!=len(str2):
    print('NOT MATCH!')
else:
    i=0
    while i < len(str1):
        if str1[i] == str2[i]:
            i += 1
        else:
            print('NOT MATCH!')
            break
    if i==len(str1):
        print('MATCH!')