import string

def rot13Encode_Decode(s):
    str1 = list(string.ascii_lowercase)
    str2 = list()  # 存储对应rot13加密后的字母
    str3 = list(string.ascii_uppercase)
    str4 = list()  # 存储对应rot13加密后的字母

    dict1 = {}  # key:小写字母    value:对应的rot13加密字母
    dict2 = {}  # key:大写字母    value:对应的rot13加密字母

    for i in range(26):
        k = i + 13
        if k <= 25:
            str2.append(str1[k])  # rot13加密算法
        else:
            str2.append(str1[k % 26])

        dict1[str1[i]] = str2[i]

    for i in range(26):
        k = i + 13
        if k <= 25:
            str4.append(str3[k])  # rot13加密算法
        else:
            str4.append(str3[k % 26])

        dict2[str3[i]] = str4[i]

    choice=input('(E)ncoding or (D)ecoding?:')
    if choice=='E':
        s1 = list(s)
        for i in range(len(s1)):
            if s1[i] in str1:
                s1[i] = dict1[s1[i]]
            if s1[i] in str3:
                s1[i] = dict2[s1[i]]

        s2 = ''.join(s1)

        print('the rot13 encode string is:', s2)  # 输出加密后的字符串

    if choice=='D':
        s1 = list(s)
        for i in range(len(s1)):
            if s1[i] in str1:
                s1[i] = get_key_by_value(dict1,s1[i])
            if s1[i] in str3:
                s1[i] = get_key_by_value(dict2,s1[i])

        s2 = ''.join(s1)

        print('the rot13 decode string is:', s2)  # 输出解密后的字符串


def get_key_by_value(dic,value):
    for key,val in dic.items():
        if val==value:
            return key


if __name__=='__main__':
    print('Welcome to rot13 translater!\n')
    s = input('please input the sting:')
    rot13Encode_Decode(s)