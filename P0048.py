import tensorflow as tf

node1 = tf.constant(3.0, tf.float32)
node2 = tf.constant(4.0, tf.float32)

@tf.function
def forward() :
    return node1+node2

out_a = forward()

#print(out_a)
#tf.print(out_a)

#print("tf version", tf.__version__)

a = tf.constant(10)
b = tf.constant(20)
c = tf.constant(30)

mul_op = (a+b)*c

print(mul_op)
tf.print(mul_op)

add_op1 = tf.add(a,b, name='add')
mul_op1 = tf.multiply(add_op1, c, name='mul')

print(mul_op1)
tf.print(mul_op1)
