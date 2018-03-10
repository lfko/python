'''
Created on 09.09.2017

@author: lfko
'''
# for guaranteeing the correct function in future python versions
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

#argument parsing
import argparse
#sys lib with different utility modules
import sys

#tensorflow mnist example data
from tensorflow.examples.tutorials.mnist import input_data



#actual tensorflow library
import tensorflow as tf

FLAGS = None

def main(_):
    
    # import data
    # creates an one-hot tensor?!
    mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
    
    # Create the model
    # first placeholder for the mnist data set
    # 50000 entries and each entry will be represented by an 784 px array (actually an image, 28x28)
    x = tf.placeholder(tf.float32, [None, 784])
    W = tf.Variable(tf.zeros([784, 10]))
    # bias?
    b = tf.Variable(tf.zeros([10]))
    # matrix multiplication x * W
    y = tf.matmul(x, W) + b
    
    # Define loss and optimizer
    y_ = tf.placeholder(tf.float32, [None, 10])
    
    # The raw formulation of cross-entropy,
    #
    #   tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(tf.nn.softmax(y)),
    #                                 reduction_indices=[1]))
    #
    # can be numerically unstable.
    #
    # So here we use tf.nn.softmax_cross_entropy_with_logits on the raw
    # outputs of 'y', and then average across the batch.
    cross_entropy = tf.reduce_mean(
        tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y))
    train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
    
    sess = tf.InteractiveSession()
    tf.global_variables_initializer().run()
    # Train
    for _ in range(1000):
        batch_xs, batch_ys = mnist.train.next_batch(100)
        sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
    
    # Test trained model
    correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    print(sess.run(accuracy, feed_dict={x: mnist.test.images,y_: mnist.test.labels}))
    
#will be called before main - e.g. to parse arguments
if __name__ == '__main__':
    #for parsing cmd arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', type=str, default='/tmp/tensorflow/mnist/input_data',
                      help='Directory for storing input data')
    FLAGS, unparsed = parser.parse_known_args()
    tf.app.run(main=main, argv=[sys.argv[0]] + unparsed)
    