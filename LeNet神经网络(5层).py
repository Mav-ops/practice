import tensorflow as  tf
import os
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.layers import Conv2D,BatchNormalization,Activation,MaxPool2D,Dropout,Flatten,Dense
from  tensorflow.keras import Model
class LeNet(Model):
    def __init__(self):
        super(LeNet,self).__init__()
        self.c1 = Conv2D(filters=5, kernel_size=(5, 5),padding='valid',
                         input_shape=(32,32,3),activation='sigmoid')
        self.p1=MaxPool2D(pool_size=(2, 2), strides=2)


        self.c2 = Conv2D(filters=16, kernel_size=(5, 5),padding='valid',
                         activation='sigmoid')
        self.p2=MaxPool2D(pool_size=(2, 2), strides=2)

        self.flatten = Flatten()
        self.f1=Dense(120, activation='sigmoid')
        self.f2=Dense(84, activation='sigmoid')
        self.f3=Dense(10, activation='softmax')

    def call(self,x):
        x = self.c1(x)
        x = self.p1(x)

        x = self.c2(x)
        x = self.p2(x)

        x = self.flatten(x)
        x = self.f1(x)
        x = self.f2(x)
        y = self.f3(x)
        return y