'''
Created on Feb 1, 2018

@author: lfko
'''

import numpy as np
from matplotlib import pyplot as plt


def main():
    # generates a 25 x 2 array, holding float values between 0 and 99
    # this is the training data
    trainData = np.random.randint(0, 100, (25, 2)).astype(np.float32)
    
    # generate class labels for the training data (either 0 or 1)
    labels = np.random.randint(0, 2, (25, 1)).astype(np.float32)
    
    # now create our first class: RED and plot it
    # ravel: kneueln
    red = trainData[labels.ravel() == 0]
    print(red)
    
    # print(trainData)
    # print(labels)
    
    plt.scatter(red[:, 0], red[:, 1], 80, 'r', '^')
    plt.show()
    
    None;


if __name__ == '__main__':
    main()
