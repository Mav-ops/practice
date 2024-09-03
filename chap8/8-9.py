def Feobanaqie(N):
    if N<=2:
        return 1
    else:
        alist = [1, 1]
        while len(alist)<=N:
            alist.append((alist[len(alist)-1]+alist[len(alist)-2]))
        return alist[N-1]

print(Feobanaqie(int(input('enter a number:'))))