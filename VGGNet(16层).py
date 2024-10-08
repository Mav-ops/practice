import tensorflow as  tf
import os
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.layers import Conv2D,BatchNormalization,Activation,MaxPool2D,Dropout,Flatten,Dense
from  tensorflow.keras import Model

class VGGNet(Model):
    def __init__(self):
        super(VGGNet, self).__init__()
        self.c1 = Conv2D(64, (3, 3), padding='same',input_shape=(32,32,3))
        self.b1 = BatchNormalization()
        self.a1=Activation('relu')
        self.c2 = Conv2D(64, (3, 3), padding='same',input_shape=(32,32,3))
        self.b2 = BatchNormalization()
        self.a2=Activation('relu')
        self.p1=MaxPool2D((2, 2), strides=2, padding='same')  #每进行一次池化操作，特征图的边长缩小为1/2
        self.d1=Dropout(0.2)

        self.c3 = Conv2D(128, (3, 3), padding='same')
        self.b3 = BatchNormalization()
        self.a3 = Activation('relu')
        self.c4 = Conv2D(128, (3, 3), padding='same')
        self.b4 = BatchNormalization()
        self.a4 = Activation('relu')
        self.p2=MaxPool2D((2, 2), strides=2, padding='same')
        self.d2 = Dropout(0.2)

        self.c5 = Conv2D(256, (3, 3), padding='same')
        self.b5 = BatchNormalization()
        self.a5 = Activation('relu')
        self.c6 = Conv2D(256, (3, 3), padding='same')
        self.b6 = BatchNormalization()
        self.a6 = Activation('relu')
        self.c7 = Conv2D(256, (3, 3), padding='same')
        self.b7 = BatchNormalization()
        self.a7 = Activation('relu')
        self.p3=MaxPool2D((2, 2), strides=2, padding='same')
        self.d3 = Dropout(0.2)

        self.c8 = Conv2D(512, (3, 3), padding='same')
        self.b8 = BatchNormalization()
        self.a8 = Activation('relu')
        self.c9 = Conv2D(512, (3, 3), padding='same')
        self.b9 = BatchNormalization()
        self.a9 = Activation('relu')
        self.c10 = Conv2D(512, (3, 3), padding='same')
        self.b10 = BatchNormalization()
        self.a10 = Activation('relu')
        self.p4 = MaxPool2D((2, 2), strides=2, padding='same')
        self.d4 = Dropout(0.2)

        self.c11 = Conv2D(512, (3, 3), padding='same')
        self.b11 = BatchNormalization()
        self.a11 = Activation('relu')
        self.c12 = Conv2D(512, (3, 3), padding='same')
        self.b12 = BatchNormalization()
        self.a12 = Activation('relu')
        self.c13 = Conv2D(512, (3, 3), padding='same')
        self.b13 = BatchNormalization()
        self.a13 = Activation('relu')
        self.p5 = MaxPool2D((2, 2), strides=2, padding='same')
        self.d5 = Dropout(0.2)

        self.flatten = Flatten()
        self.f1 = Dense(512, activation='relu')
        self.d6 = Dropout(0.2)
        self.f2 = Dense(512, activation='relu')
        self.d7 = Dropout(0.2)
        self.f3 = Dense(10, activation='softmax')

    def call(self, x):
        x = self.c1(x)
        x = self.b1(x)
        x = self.a1(x)

        x = self.c2(x)
        x = self.b2(x)
        x = self.a2(x)
        x = self.p1(x)
        x = self.d1(x)

        x = self.c3(x)
        x = self.b3(x)
        x = self.a3(x)

        x = self.c4(x)
        x = self.b4(x)
        x = self.a4(x)
        x = self.p2(x)
        x = self.d2(x)

        x = self.c5(x)
        x = self.b5(x)
        x = self.a5(x)

        x = self.c6(x)
        x = self.b6(x)
        x = self.a6(x)

        x = self.c7(x)
        x = self.b7(x)
        x = self.a7(x)
        x = self.p3(x)
        x = self.d3(x)

        x = self.c8(x)
        x = self.b8(x)
        x = self.a8(x)

        x = self.c9(x)
        x = self.b9(x)
        x = self.a9(x)

        x = self.c10(x)
        x = self.b10(x)
        x = self.a10(x)
        x = self.p4(x)
        x = self.d4(x)

        x = self.c11(x)
        x = self.b11(x)
        x = self.a11(x)

        x = self.c12(x)
        x = self.b12(x)
        x = self.a12(x)

        x = self.c13(x)
        x = self.b13(x)
        x = self.a13(x)
        x = self.p5(x)
        x = self.d5(x)

        x = self.flatten(x)
        x = self.f1(x)
        x = self.d6(x)
        x = self.f2(x)
        x = self.d7(x)
        y = self.f3(x)
        return y

