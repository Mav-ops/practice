'''预测酸奶销量'''
import tensorflow as tf
import numpy as np

rdm = np.random.RandomState(seed=256)
x = rdm.rand(100, 2)

y_ = [[x1 + x2 - (rdm.rand() / 10 - 0.5)] for (x1, x2) in x]
x = tf.cast(x, dtype=tf.float32)

cost = 1
profit = 99
epoch = 10000
lr = 0.002

w1 = tf.Variable(tf.random.normal([2, 1], stddev=1, seed=1))

for epoch in range(epoch):
    with tf.GradientTape() as tape:
        y = tf.matmul(x, w1)
        loss = tf.reduce_sum(tf.where(tf.greater(y, y_), cost * (y - y_), profit * (y_ - y)))
    grads = tape.gradient(loss, w1)
    w1.assign_sub(lr * grads)

    if epoch % 500 == 0:
        print('Epoch:%d,w1 is', epoch)
        print(w1.numpy(), '\n')

print('final w1 is', w1.numpy())



