import tensorflow as tf

x = tf.constant(5)
y = tf.constant(6)

result = tf.multiply(x,y)
# start a new session
sess = tf.Session() # grab a session object
print(sess.run(result))
