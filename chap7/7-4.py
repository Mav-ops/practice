a=[1,2,3,4,5,6,7]
b=['abc','def','ghi','jkl','mno','pqr','stu']
dict1={}
dict2={}
for i in range(len(a)):
    dict2={a[i]:b[i]}
    dict1.update(dict2)

print(dict1)