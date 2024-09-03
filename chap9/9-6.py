f1=input('Enter a filename: ')
f2=input('Enter a filename: ')
F1=open(f1,'r')
F2=open(f2,'r')
F1alline=F1.readlines()
F2alline=F2.readlines()
F1.close()
F2.close()
len1=len(F1alline)
len2=len(F2alline)
minlen=min(len1,len2)
bool1=False
for i in range(minlen):
   # print(F1alline[i],F2alline[i])
    if F1alline[i]!=F2alline[i]:
        minlen2=min(len(F1alline[i]),len(F2alline[i]))
        for j in range(minlen2):
            if F1alline[i][j]!=F2alline[i][j]:
                bool1=True
                print('row is %d,column is %d'%(i+1,j+1))
                break
    else:
        continue

if bool1==False:
    if len1==len2:
        print('They are equal.')
    else:
        print('row is %d,column is %d'%(minlen,minlen2+1))
