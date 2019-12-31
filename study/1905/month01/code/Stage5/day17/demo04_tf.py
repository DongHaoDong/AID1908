"""
demo04_tf.py    创建变量
"""
import tensorflow as tf
# 输入层
x = tf.constant(
    [[1, 3], [4, 6], [8, 6], [9, 3]], name='x',
    dtype='float32')
# 第一层权重
w0 = tf.Variable(tf.random_normal(
    [2, 4], stddev=0.35, mean=0, seed=1), name='w0',
    dtype='float32')
# 第二层权重
w1 = tf.Variable(tf.random_normal(
    [4, 1], stddev=0.35, mean=0, seed=1), name='w1',
    dtype='float32')
# 整理前向网络结构
l1 = tf.matmul(x, w0)
l2 = tf.matmul(l1, w1)
# 执行计算图
init_op = tf.initialize_all_variables()
with tf.Session() as sess:
    sess.run(init_op)  # 初始化所有的Variable对象
    r = sess.run(l2)
    print(r)
