import tensorflow as tf
from tensorflow.keras import Model
from tensorflow.keras.layers import Dense,Flatten

fashion_mnist = tf.keras.datasets.fashion_mnist
(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
x_train = x_train / 255.0
x_test = x_test / 255.0

class FashionModel(Model):
    def __init__(self):
        super(FashionModel, self).__init__()
        self.flatten = Flatten()
        self.d1 = Dense(256, activation='relu')
        self.d2 = Dense(128, activation='relu')
        self.out = Dense(10, activation='softmax')

    def call(self, inputs):
        x = self.flatten(inputs)
        x = self.d1(x)
        x = self.d2(x)
        x = self.out(x)
        return x

model = FashionModel()

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),
              metrics=['sparse_categorical_accuracy'])

model.fit(x_train, y_train, epochs=10,
          validation_data=(x_test, y_test),
          validation_freq=1)

model.summary()