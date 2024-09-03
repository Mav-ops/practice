
def tr(srcstr,dststr,string,c):
    dict1={}
    if c==1:  #区分大小写
        if len(srcstr) < len(dststr):
            print('字符数不合，无法翻译')
        else:
            for i in range(len(dststr)):
                dict1[srcstr[i]] = dststr[i]

        str1 = list(string)

        for j in range(len(str1)):
            if str1[j] in dict1.keys():
                str1[j] = dict1[str1[j]]
            if str1[j] not in dict1.keys() and str1[j] in srcstr:
                str1[j]=''
        str2 = ''.join(str1)
        print(str2)

    if c==0: #不区分大小写
        if len(srcstr) < len(dststr):
            print('字符数不合，无法翻译')
        else:
            for i in range(len(dststr)):
                dict1[srcstr[i].lower()] = dststr[i]

        str1 = list(string.lower())

        for j in range(len(str1)):
            if str1[j] in dict1.keys():
                str1[j] = dict1[str1[j].lower()]
            if str1[j] not in dict1.keys() and str1[j] in srcstr.lower():
                str1[j]=''
        str2 = ''.join(str1)
        print(str2)

if __name__=='__main__':
    string=input('输入要翻译的字符串：')
    srcstr=input('输入要翻译的字符：')
    dststr=input('输入翻译后的字符：')
    c=int(input('是否区分大小写？1：是；0：否'))
    tr(srcstr,dststr,string,c)