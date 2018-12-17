'''
Created on Dec 13, 2018

@author: fb
    
    Simple Re-implementation of the infamous Rosenblatt Perceptron

'''

import random
from sklearn.datasets import load_digits


class SLPClassifier():
    '''

    '''

    def __init__(self):

        self.learn_rate = 0.1
        self.weights = []
        self.epochs = 10
        self.bias = 1
        print(' Classifier initialised ')
        '''
            Each datapoint is a 8x8 image of a digit.
    
            =================   ==============
            Classes                         10
            Samples per class             ~180
            Samples total                 1797
            Dimensionality                  64
            Features             integers 0-16
            =================   ==============
        '''
        # digits = load_digits()
        # print(digits.images[0])
        # print(digits.target[0])

        # import matplotlib.pyplot as plt
        # plt.gray() # doctest: +SKIP
        # plt.matshow(digits.images[0]) # doctest: +SKIP
        # plt.show() # doctest: +SKIP

    def train(self, train_data, labels, epochs, learn_rate=0.05):
        """ """
        self.weights = [0.0 for i in range(len(train_data[0]))]
        for epoch in range(epochs):
            sum_error = 0.0

            for i, row in enumerate(train_data):
                # predict the value for the current weight and row
                print(row[0])
                predicted = self.doBinary(row)
                error = labels[i] - predicted  # calculate the error
                sum_error += error ** 2  # for getting only positive values

                # self.weights[0] = self.weights[0] + learn_rate * error #
                # update the bias?
                self.bias = self.bias + learn_rate * error
                for i in range(len(row) - 1):
                    self.weights[i] = self.weights[i] + \
                        self.learn_rate * error * row[i]
                    print('>epoch=%d, lrate=%.3f, error=%.3f, bias=%.3f' %
                          (epoch, learn_rate, sum_error, self.bias))

        # the layer had been trained
        print('current weights ', self.weights)

    def predict(self, work_data):

        correct = 0

        for row in work_data:
            predicted = self.doBinary(row)
            print('predicted: ', predicted, ' and actual ', row[-1])
            if predicted == row[-1]:
                correct += 1

        accuracy = (correct / len(work_data)) * 100.0
        print('achieved accuray ', accuracy)

    def doBinary(self, input_vec):
        """ do classification, based on a one-against-all approach.
            Based on the summed up value, applying a specific function and/or threshold """

        # input x_0 is the bias, i.e. a constant value
        # bias = 1.0

        # since the label is part of the input vector, we only for-loop the
        # (len-1)-th element
        for i in range(len(input_vec) - 1):
            activation = self.weights[i] * input_vec[i] + self.bias
            # print(activation)

        return 1.0 if activation >= 0.0 else 0.0

    def doMulticlass(self):
        """ do classification, based on multiple classes """


X, Y = load_digits(n_class=10, return_X_y=True)
print(X)
print(Y)

digits = load_digits()
# print(digits.images[0])
# print(digits.target[0])

slpc = SLPClassifier()
print('train', slpc.train(digits.images, digits.target, learn_rate=0.3, epochs=100))
"""

slpc = SLPClassifier()
myData = []
for i in range(20):
    myData.append(
        [round(random.uniform(1, 10), 5), round(random.uniform(1, 10), 5), round(random.uniform(1, 10), 5), random.randint(0, 1)])
print(myData)
print(len(myData[0]))
# for row in myData:
print('train', slpc.train(myData, learn_rate=0.3, epochs=100))
myData = []
for i in range(20):
    myData.append(
        [round(random.uniform(1, 10), 5), round(random.uniform(1, 10), 5), round(random.uniform(1, 10), 5), random.randint(0, 1)])
slpc.predict(myData)

"""
