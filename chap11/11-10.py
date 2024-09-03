# -*- coding: utf-8 -*-
def cleanfile(lines):
    li = map(lambda x:x.strip(),lines)
    #列表解析
    #li = [x.strip() for x in lines]
    return li

if __name__ == '__main__':
    order = input('new or old')
    # name = input('filename')
    # f = open(name, 'r')
    # lines = f.readlines()
    # f.close()
    # li = cleanfile(lines)

    if order == 'new':
        file2 = input('newfile')
        f = open(file2, 'w')
        while True:
            i=input('enter your contents:')
            if i=='.':
                break
            f.write(i)
        f.close()
        f = open(file2, 'r')
        lines = f.readlines()
        f.close()
        li = cleanfile(lines)

    else:
        name = input('filename')
        file2 = name
        f = open(name, 'r')
        lines = f.readlines()
        f.close()
        li = cleanfile(lines)
    f = open(file2, 'w')
    for i in li:
        f.write(i)
        f.write('\n')
    f.close()