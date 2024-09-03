def fun1(li,li2):
    re={}
    for i in range(len(li)):
        re[str(li[i])+'+'+str(li2[i])+'=']=li[i]+li2[i]
    return re

if __name__=='__main__':
    li=[1,2,3,4]
    li2=[5,6,7,8]
    re=fun1(li,li2)
    for eachkey in re:
        print(eachkey,re[eachkey])