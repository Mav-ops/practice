import numpy as np
#定义参数
x1=np.array(2)
x2=np.array(3)
w11,w12,w21,w22=np.array([2,0.5,2,0.5])
b11,b12,b2=np.array([1,1,1])
w1=np.array(2)
w2=np.array(-1)
lr=0.01
Y=4
#定义激活函数
def relu(z):
    if z<=0:
        return 0
    else:
        return z

#前向传播
z1=x1*w11+x2*w12+b11
z2=x1*w21+x2*w22+b12
a1=relu(z1)
a2=relu(z2)
y=a1*w1+a2*w2+b2

#计算损失
Loss=pow((y-Y),2)/2
print(Loss)
while Loss >0.1:
    z1 = x1 * w11 + x2 * w12 + b11
    z2 = x1 * w21 + x2 * w22 + b12
    a1 = relu(z1)
    a2 = relu(z2)
    y = a1 * w1 + a2 * w2 + b2

    # 计算损失
    Loss = pow((y - Y), 2) / 2
    print('Loss:',Loss)
    #梯度下降更新参数
    w11_grad=(y*w1*1*x1)
    if w11_grad==0:
        break
    print('gradient:',w11_grad)
    w11=w11-lr*w11_grad
    print('updated:',w11)