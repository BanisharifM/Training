import tensorflow as tf
tf.compat.v1.disable_eager_execution()
x = tf.compat.v1.placeholder(tf.float32)
# x = tf.placeholder("float", None)
y = x * 2

with tf.compat.v1.Session() as session:
    result = session.run(y, feed_dict={x: [1, 2, 3]})
    print(result)
