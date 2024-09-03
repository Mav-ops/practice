x=input('input a complex:')
l=len(x)
fuhao=['+','-']
a='123'
b='123'
if x[-1]!='j':
    print("error ,input the correct complex.")
else:
    print(x)
    for i in range(-2,-len(x),-1):
        if x[i] in fuhao:
            a=x[:i]
            b=x[i:-1]
            print(a)
            print(b)
            c = complex(float(a),float(b))
            print(c)
            break

'''
当两个参数都不提供时，返回复数 0j。

当第一个参数为字符串时，调用时不能提供第二个参数。

当第一个参数为int或者float时，第二个参数可为空，表示虚部为0；
如果提供第二个参数，第二个参数也需为int或者float。
'''

