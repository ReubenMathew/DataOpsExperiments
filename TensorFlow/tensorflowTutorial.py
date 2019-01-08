import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
sess = tf.Session()

x1 = tf.constant([1,4,4,5])
x2 = tf.constant([2,5,1,6])

result = tf.multiply(x1,x2)

with tf.Session() as sess:
	output = sess.run(result)
	print(output)

