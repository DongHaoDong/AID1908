"""
demo03_tf.py tensorflow基础
"""
import tensorflow as tf

a = tf.constant([1.0,2.0],name='a')
b = tf.constant([2.0,3.0],name='b')
print(a)
print(b)
result = a + b
print(result)
result = tf.add(a,b,name='Add')
print(result)
# 使用tf.Session()运行计算图
sess = tf.Session()
r = sess.run(result)
print(r)
print(type(sess.run(a)))
sess.close()
# 使用with语句，运行计算图
with tf.Session() as sess:
    print(sess.run(result * 2))