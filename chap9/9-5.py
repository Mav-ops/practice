scores = []
while True:
    fname = input('Enter filename: ')
    if fname==None:
        break
    f = open(fname, 'r')
    for i in f:
        if 0 <= int(i.strip()) <= 100:
            scores.append(int(i.strip()))
        else:
            print('score wrong,please check the file.')
        if int(i.strip()) < 60:
            print('score is E', i)
        elif int(i.strip()) < 70:
            print('score is D', i)
        elif int(i.strip()) < 80:
            print('score is C', i)
        elif int(i.strip()) < 90:
            print('score is B', i)
        else:
            print('score is A', i)
    f.close()

print('average score is %.2f'%(sum(scores)/len(scores)))