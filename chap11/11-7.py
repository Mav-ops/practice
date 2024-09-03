li=[1,2,3]
li2=['abc','def','ghi']
list1=[]
list2=[]
list1.extend(map(lambda x,y:(x,y),li,li2))
list2.extend(zip(li,li2))
print(list1)
print(list2)

