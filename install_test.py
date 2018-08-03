#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
# Importing tensorflow
import tensorflow as tf

sess = tf.Session()

hello = tf.constant("Hello World!")
print(sess.run(hello))

a = tf.constant(20)
b = tf.constant(40)
print('a + b = {0}'.format(sess.run(a+b)))
