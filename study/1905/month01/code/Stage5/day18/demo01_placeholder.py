"""
deemo01_placeholder.py  占位符
"""
import tensorflow as tf

x = tf.placeholder(tf.float32, shape=(None, 2))
w0 = tf.constant(
    [[1, 2, 3, 4], [5, 6, 7, 8]], dtype='float32')
w1 = tf.constant(
    [[2], [3], [2], [1]], dtype='float32')
l1 = tf.matmul(x, w0)
out = tf.matmul(l1, w1)

with tf.Session() as sess:
    r = sess.run(out, feed_dict={x: [[5., 6.]]})
    print(r)
    r = sess.run(out, feed_dict={x: [[6., 5.]]})
    print(r)
    r = sess.run(out, feed_dict={x: [[5., 6.], [6., 5.]]})
    print(r)