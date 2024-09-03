def muPop():
    a=[]
    a.extend(list(map(str,input('输入列表元素：').split(','))))
    a=a[:len(a)-1]
    return a

print(muPop())
