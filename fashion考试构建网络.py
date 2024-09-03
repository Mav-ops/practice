import tensorflow as tf
from PIL import Image
import numpy as np
import os
import matplotlib.pyplot as plt

train_path = 'C:/Users/Mav/PycharmProjects/pythonProject/fashion_image_label/fashion_train_jpg_60000'
train_txt='C:/Users/Mav/PycharmProjects/pythonProject/fashion_image_label/fashion_train_jpg_60000.txt'
x_train_savepath='C:/Users/Mav/PycharmProjects/pythonProject/fashion_image_label/fashion x_train.npy'
y_train_savepath='C:/Users/Mav/PycharmProjects/pythonProject/fashion_image_label/fashion y_train.npy'

test_path='C:/Users/Mav/PycharmProjects/pythonProject/fashion_image_label/fashion_test_jpg_10000'
test_txt='C:/Users/Mav/PycharmProjects/pythonProject/fashion_image_label/fashion_test_jpg_10000.txt'
x_test_savepath='C:/Users/Mav/PycharmProjects/pythonProject/fashion_image_label/fashion_x_test.npy'
y_test_savepath='C:/Users/Mav/PycharmProjects/pythonProject/fashion_image_label/fashion_y_test.npy'

def generateds(path,txt):
    f = open(txt,'r')
    contents = f.readlines()
    f.close()
    x,y_=[],[]
    i=0
    for content in contents:
        value=content.split()
        img_path=path+'/'+ value[0]
        img=Image.open(img_path)
        img=np.array(img.convert('L'))
        img=img/255.0
        x.append(img)
        y_.append(value[1])
        if i%1000==0:
            print('Loading :'+ content)
        i+=1

    x=np.array(x)
    y_=np.array(y_)
    y_=y_.astype(np.int64)
    return x,y_

if os.path.exists(x_train_savepath) and os.path.exists(
        y_train_savepath) and os.path.exists(
    x_test_savepath) and os.path.exists(y_test_savepath):
    print('-----------------Load Datasets-------------------')
    x_train_save=np.load(x_train_savepath)
    y_train=np.load(y_train_savepath)
    x_test_save=np.load(x_test_savepath)
    y_test=np.load(y_test_savepath)
    x_train=np.reshape(x_train_save,(len(x_train_save),28,28))
    x_test=np.reshape(x_test_save,(len(x_test_save),28,28))
else:
    print('-----------------Generate Datasets------------------')
    x_train,y_train=generateds(train_path,train_txt)
    x_test,y_test=generateds(test_path,test_txt)

    print('---------------Save Datasets-------------------')
    x_train_save=np.reshape(x_train,(len(x_train),-1))
    x_test_save=np.reshape(x_test,(len(x_test),-1))
    np.save(x_train_savepath,x_train_save)
    np.save(y_train_savepath,y_train)
    np.save(x_test_savepath,x_test_save)
    np.save(y_test_savepath,y_test)

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])


model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),
              metrics=['sparse_categorical_accuracy'])

checkpoint_save_path = './checkpoint/fashion.ckpt'
if os.path.exists(checkpoint_save_path + '.index'):
    print('----------------------load the model------------------')
    model.load_weights(checkpoint_save_path)

cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_save_path,
 save_weights_only=True,save_best_only=True
)

history = model.fit(x_train,y_train,batch_size=32,epochs=5,
          validation_data=(x_test,y_test),validation_freq=1,callbacks=[cp_callback])

model.summary()


acc=history.history['sparse_categorical_accuracy']
val_acc=history.history['val_sparse_categorical_accuracy']
loss=history.history['loss']
val_loss=history.history['val_loss']

plt.subplot(1,2,1)
plt.plot(acc, label='Training Accuracy')
plt.plot(val_acc, label='Validation Accuracy')
plt.title('Training and Validation Accuracy')
plt.legend()

plt.subplot(1,2,2)
plt.plot(loss, label='Training Loss')
plt.plot(val_loss, label='Validation Loss')
plt.title('Training and Validation Loss')
plt.legend()
plt.show()