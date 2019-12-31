import tensorflow as tf
import numpy as np
import sklearn.datasets as datasets
import matplotlib.pyplot as mp
BATCH_SIZE = 8

X, Y = datasets.make_moons(200, noise=0.10)
Y = np.array(np.column_stack((Y, ~Y+2)), dtype='f4')
print(Y)

#定义神经网络的输入、参数和输出，定义向前传播过程
x = tf.placeholder(tf.float32, shape=(None,2), name='x')
y = tf.placeholder(tf.float32, shape=(None,2), name='y')

w1 = tf.Variable(tf.random_normal((2,3),stddev=1,seed=1))
b1 = tf.Variable(tf.random_normal((3,),stddev=1,seed=1))
w2 = tf.Variable(tf.random_normal((3,2),stddev=1,seed=1))
b2 = tf.Variable(tf.random_normal((2,),stddev=1,seed=1))

l1 = tf.nn.sigmoid(tf.add(tf.matmul(x,w1), b1))
y_ = tf.add(tf.matmul(l1,w2), b2)

#定义损失函数及反向传播方法
loss = tf.reduce_sum(tf.nn.softmax_cross_entropy_with_logits(labels=y,logits=y_))
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(loss)
#train_step=tf.train.AdamOptimizer(0.001).minimize(loss)

#生成会话，训练STEPS轮
with tf.Session() as sess:
    init_op=tf.global_variables_initializer()
    sess.run(init_op)

    #训练模型
    STEPS = 30000
    for i in range(STEPS):
        start = (i*BATCH_SIZE) % 32
        end = start + BATCH_SIZE
        sess.run(train_step,feed_dict={x:X[start:end], y:Y[start:end]})
        if i % 500 ==0:
            total_loss = sess.run(loss,feed_dict={x:X, y:Y})
            print("After %d training steps, loss on all data is %g"%(i,total_loss))

    pred_y = sess.run(y_, feed_dict={x:X})
    pred_y = np.piecewise(pred_y, [pred_y<0, pred_y>0], [0, 1])

    l, r = X[:, 0].min() - 1, X[:, 0].max() + 1
    b, t = X[:, 1].min() - 1, X[:, 1].max() + 1
    n = 500
    grid_x, grid_y = np.meshgrid(np.linspace(l, r, n), np.linspace(b, t, n))
    samples = np.column_stack((grid_x.ravel(), grid_y.ravel()))

    grid_z = sess.run(y_, feed_dict={x:samples})
    grid_z = grid_z.reshape(-1, 2)[:,0]
    grid_z = np.piecewise(grid_z, [grid_z<0, grid_z>0], [0, 1])
    grid_z = grid_z.reshape(grid_x.shape)
    mp.figure('Logistic Classification', facecolor='lightgray')
    mp.title('Logistic Classification', fontsize=20)
    mp.xlabel('x', fontsize=14)
    mp.ylabel('y', fontsize=14)
    mp.tick_params(labelsize=10)
    mp.pcolormesh(grid_x, grid_y, grid_z, cmap='gray')
    mp.scatter(X[:, 0], X[:, 1], c=Y[:,0], cmap='brg', s=80)
    mp.show()