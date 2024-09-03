'''
numpy.random.seed()
seed( ) 函数用于指定随机数生成时所用算法开始的整数值，如果使用相同的 seed() 值，则每次生成的随机数都相同，
如果不设置这个值，则系统根据时间来自己选择这个值，此时每次生成的随机数因时间差异而不同。

t_params = tf.get_collection('target_net_params')
e_params = tf.get_collection('eval_net_params')   从一个集合中取出变量


更新Target Net
self.replace_target_op = [tf.assign(t, e) for t, e in zip(t_params, e_params)]
tf.assign(t, e)   把e的值给t

tf.Session(self, target='', graph=None, config=None)  创建一个新的TensorFlow会话。
如果在构造会话时未指定`graph`参数，则默认图将在会话中启动。 如果在同一过程中使用多个图（通过tf.Graph（）创建），
则每个图必须使用不同的会话，但是每个图可以在多个会话中使用。在这种情况下，将要显式启动的图传递给会话构造函数通常更为清晰。

tf.summary.FileWriter("logs/", self.sess.graph)
指定一个文件用来保存图。

sess = tf.Session()
sess.run(tf.global_variables_initializer())
初始化模型的参数
训练神经网络的时候，总会加上tf.global_variables_initializer().run()
或者 sess.run(tf.global_variables_initializer())

tf.compat.v1.placeholder(dtype,shape=None,name=None)
placeholder是占位符，相当于定义了一个变量，提前分配了需要的内存。但只有启动一个session，程序才会真正的运行。
建立session后，通过feed_dict()函数向变量赋值。
 dtype数据类型、shape数据形状、name名称

'''
# import tensorflow as tf
#
# tensorflow_version = tf.__version__
# gpu_available = tf.test.is_gpu_available()
#
# print('tensorflow version:', tensorflow_version,
#       '\tgpu_available:', gpu_available)
#
# a=tf.constant([1.0,2.0],name='a')
# b=tf.constant([1.0,2.0],name='b')
# result=tf.add(a,b,name='add')
# print(result)

x=[]
li=[1,2,3,4,5,6,7,8,9]
for i in range(3,len(li)):
   x.append(li[i-3:i])

print(x)