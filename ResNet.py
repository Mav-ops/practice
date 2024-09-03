import tensorflow as  tf
import os
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.layers import Conv2D,BatchNormalization,Activation,MaxPool2D,Dropout,Flatten,Dense
from  tensorflow.keras import Model
from tensorflow_core.python.keras.layers import GlobalAveragePooling2D


class ResnetBlock(Model):
    def __init__(self,filters,strides=1,residual_path=False):
        super(ResnetBlock,self).__init__()
        self.filters = filters
        self.strides = strides
        self.residual_path = residual_path

        self.c1 = Conv2D(filters=filters,kernel_size=(3,3),strides=strides,padding='same',use_bias=False)
        self.b1 = BatchNormalization()
        self.a1 = Activation('relu')
        self.c2 = Conv2D(filters=filters,kernel_size=(3,3),strides=strides,padding='same',use_bias=False)
        self.b2 = BatchNormalization()
        #residual_path为True时，对输出进行下采样，即用1*1的卷积核做卷积操作，保证x能和F(x)维度相同，顺利相加
        if residual_path:
            self.down_c1 = Conv2D(filters=filters,kernel_size=(1,1),strides=strides,padding='same',use_bias=False)
            self.down_b1 = BatchNormalization()

        self.a2 = Activation('relu')

    def call(self,inputs):
        residual = inputs    #residual等于输入值本身，即residual=x
        #将输入通过卷积，BN层，激活曾，计算F(x)
        x = self.c1(inputs)
        x = self.b1(x)
        x = self.a1(x)

        x = self.c2(x)
        y = self.b2(x)

        if self.residual_path:
            residual = self.down_c1(inputs)
            residual = self.down_b1(residual)

        out = self.a2(y+residual)   #最后输出两部分的和，即F(x)+x或F(x)+W(x)
        return out


class ResNet18(Model):
    def __init__(self,block_list,initial_filters=64): #block_list表示每个block有几个卷积层
        super(ResNet18,self).__init__()
        self.num_blocks = len(block_list) #共有几个block
        self.block_list = block_list
        self.out_filters = initial_filters

        self.c1 = Conv2D(self.out_filters,kernel_size=(3,3),strides=1,padding='same',use_bias=False,
                         kernel_initializer='he_normal')
        self.b1 = BatchNormalization()
        self.a1 = Activation('relu')
        self.blocks = tf.keras.models.Sequential()
        #构建ResNet网络结构
        for block_id in range(self.num_blocks):  #第几个resnet block
            for layer_id in range(block_list[block_id]):  #第几个卷积层

                if block_id!=0 and layer_id == 0:  #对除第一个blocky以外的每个block的输入进行行下采样
                    block = ResnetBlock(self.out_filters,strides=2,residual_path=True)
                else:
                    block = ResnetBlock(self.out_filters,residual_path=False)
                self.blocks.add(block) #将构建好的block加入resnet
            self.out_filters *= 2 #下一个block的卷积核数是上一个block的2倍

        self.p1 = GlobalAveragePooling2D()
        self.f1 = Dense(10, activation='softmax')

    def call(self,inputs):
        x = self.c1(inputs)
        x = self.b1(x)
        x = self.a1(x)
        x = self.blocks(x)
        x = self.p1(x)
        y = self.f1(x)
        return y

model = ResNet18(block_list=[2,2,2,2])
