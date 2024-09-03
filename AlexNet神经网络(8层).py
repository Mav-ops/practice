import tensorflow as  tf
import os
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.layers import Conv2D,BatchNormalization,Activation,MaxPool2D,Dropout,Flatten,Dense
from  tensorflow.keras import Model

class AlexNet(Model):
    def __init__(self):
        super(AlexNet, self).__init__()
        self.c1 = Conv2D(filters=96, kernel_size=(3,3),input_shape=(32,32,3))
        self.b1 = BatchNormalization()
        self.a1= Activation('relu')     #relu函数增加了模型训练速度
        self.p1=MaxPool2D(pool_size=(3,3),strides=2)

        self.c2 = Conv2D(filters=256, kernel_size=(3,3))
        self.b2 = BatchNormalization()
        self.a2= Activation('relu')
        self.p2=MaxPool2D(pool_size=(3,3),strides=2)

        self.c3 = Conv2D(filters=384, kernel_size=(3,3),
                         padding='same',activation='relu')

        self.c4=Conv2D(filters=384, kernel_size=(3,3),
                       padding='same',activation='relu')

        self.c5=Conv2D(filters=256, kernel_size=(3,3),
                       padding='same',activation='relu')
        self.p3=MaxPool2D(pool_size=(3,3),strides=2)

        self.flatten = Flatten()
        self.f1 = Dense(2048, activation='relu')
        self.d1=Dropout(0.5)         #防止过拟合  提升了鲁棒性（英语：robustness，音譯），指事物可以抵御外部应力和影响并维持原有状态的自身性质，与汉语中的“稳健性”或“坚韧性”同义。
        self.f2=Dense(2048, activation='relu')
        self.d2=Dropout(0.5)         #防止过拟合
        self.f3=Dense(10, activation='softmax')

    def call(self,x):
        x = self.c1(x)
        x = self.b1(x)
        x = self.a1(x)
        x = self.p1(x)

        x = self.c2(x)
        x = self.b2(x)
        x = self.a2(x)
        x = self.p2(x)

        x = self.c3(x)

        x = self.c4(x)

        x = self.c5(x)
        x = self.p3(x)

        x = self.flatten(x)
        x = self.f1(x)
        x = self.d1(x)
        x = self.f2(x)
        x = self.d2(x)
        y = self.f3(x)

        return y