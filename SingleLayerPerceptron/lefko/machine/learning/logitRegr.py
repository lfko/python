'''
Created on Dec 15, 2018

@author: Florian "lfko" Becker
'''
import numpy as np
from sklearn.datasets import load_digits


class LogitRegrClassifier():
    '''

    '''

    def __init__(self):
        '''

        '''

    def predict(self, x, w):
        """ """

        z = 0.0  # logit
        # y = 0  # predicted value

        # print('#######')
        #print('x ', x)
        #print('w ', w)
        # print('#######')

        for i in range(len(x)):
            z += x[i] * w[i]

        # binary threshold classifier
        return 0 if z < 0.0 else 1

    def train(self, train_data, data_label, old_w, epochs=10, learn_rate=0.5):
        """ """
        # print(data_label)
        #new_w = np.array([np.random.uniform(-0.5, 0.5, len(train_data[0]))])
        w = old_w
        y_exp = 0
        sum_correct = 0

        for epoch in range(epochs):
            print(' start training for epoch #', epoch)
            for i in range(len(train_data)):
                #print('i', i)
                # print(train_data[i])
                y = self.predict(train_data[i], w)
                y_exp = data_label[i]
                #print('predicted value ', y, ' expected value ', y_exp)
                if y == y_exp:
                    #print(' value correctly predicted ')
                    sum_correct += 1
                elif y != y_exp:
                    if y > y_exp:
                        w = train_data[i] - w * learn_rate
                    else:
                        w = train_data[i] + w * learn_rate

            print(' final adjusted weight vector ', w)
            print('>>> final accuracy: ',
                  (sum_correct / len(data_label) * 100), ' <<<')
            sum_correct = 0.0

        return w


my_Vec = np.ones(20)
my_Vec = my_Vec[:, np.newaxis]
# print(my_Vec)

data = np.random.uniform(0, 5, size=(20, 2))
#b = np.transpose(np.array([0, 0]))
# print(b)
#print(np.array([0, 0]).reshape((2, 1)))
#c = np.array([1, 1]).reshape((20, 1))
x = np.append(data, my_Vec, axis=1)
# print(data)
print('input: ')
print(x)
labels = np.random.randint(0, 2, size=(20, 1))
print(' labels ')
print(labels)

w = np.array(np.random.uniform(-0.5, 0.5, len(x[0])))
print('initial neuron weights (randomly created)', w)
logRegr = LogitRegrClassifier()
trained_w = logRegr.train(x, labels, w)

real_data = np.random.uniform(-5, 5, size=(50, 2))
real_input = np.append(real_data, np.ones(50)[:, np.newaxis], axis=1)
real_labels = np.random.randint(0, 2, size=(50, 1))
real_acc = 0.0
sum_correct = 0
for i in range(len(real_input)):
    y_pred = logRegr.predict(real_input[i], trained_w)
    y_real = real_labels[i]
    print('predicted value ', y_pred, ' expected value ', y_real)
    sum_correct += 1 if y_pred == y_real else 0

print(' real data accuracy ', (sum_correct / len(real_input)) * 100)
