import os
import tensorflow as tf

# turning off tf warning
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# defining computation graph
X = tf.placeholder(tf.float32, name="X")
Y = tf.placeholder(tf.float32, name="Y")
addition = tf.add(X, Y, name="addition")

# creating a session 
with tf.Session() as session:
    result = session.run(addition, feed_dict={X: [1,3,4,5], Y: [4,7,8,8]})
    print(result)