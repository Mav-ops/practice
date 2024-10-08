import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

fashion_mnist = tf.keras.datasets.fashion_mnist
(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

x_train=x_train.reshape(x_train.shape[0],28,28,1)

###################################################
image_gen_train = ImageDataGenerator(            ##
    rescale=1./1.,                               ##
    rotation_range=45,                           ##
    width_shift_range=0.15,
    height_shift_range=0.15,
    horizontal_flip=True,
    zoom_range=0.5,
)

image_gen_train.fit(x_train)                      ##
####################################################

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),
              metrics=['sparse_categorical_accuracy'])

##############################################################################
model.fit(image_gen_train.flow(x_train, y_train, batch_size=32),epochs=5,
          validation_data=(x_test, y_test),validation_freq=1)



model.summary()