'''
Created on Nov 7, 2018

@author: fb (s76343)
'''

import numpy as np


def assignment_03_01():
    """ creates a one-dimensional numpy array with numbers from 0 - 30, stepping 3 """
    # be aware, that arange() only generates values exclusiv of the stop value
    return np.arange(0, 33, 3)


def assignment_03_02():
    """ Write a function assignment_03_02 that creates a numpy array with 4 rows and 5 columns. The
        content of the array should be 1 for all cells initially. Then, the function should multiply each
        column by its column index plus 1 and then subtracts its row index. """

    # creates a 4 row, 5 column array, containing only 1
    npArr = np.ones((4, 5), dtype=int)
    # multiply the array with a vector containing numbers 1 - 5 and afterwards
    # substract a matrix, containing the row indexes as row values
    npArr = npArr * [1, 2, 3, 4, 5] - np.array([np.linspace(0, 0, 5), np.linspace(
        1, 1, 5), np.linspace(2, 2, 5), np.linspace(3, 3, 5)])

    return npArr


def assignment_03_03(npArr):
    """ function that expects a numpy array with 4 rows and 5 columns. Then, extract a (2,3) subarray and return it """

    # checking the shape of the array
    if(np.shape(npArr) != (4, 5)):
        raise ValueError(' not the right shape - I need 4 rows and 5 columns')
    else:
        print('I can work with that')

    # for testing
    # npArr = npArr * [1, 2, 3, 4, 5] - np.array([np.linspace(0, 0, 5), np.linspace(1, 1, 5), np.linspace(2, 2, 5), np.linspace(3, 3, 5)])
    # [:2, :3] - two rows three columns
    # [1:5, 1:5]

    # slice the subarray: 2 rows and 3 columns, beginning with the second
    # column
    arraySlice = npArr[1:3, 1:4]

    return arraySlice


def assignment_03_04():
    """ 
    function that creates a numpy array with 100000 rows and 2 columns. The first column should contain Gaussian distributed variables with
    mean 1 and standard deviation 2 and the second column should contain Gaussian distributed variables with mean -2 and standard deviation 0.5. """

    # each call creates a normal (gaussian) distributed np.array with given
    # properties and size 100.000

    col1 = np.random.normal(1, 2, 100000)  # vector col1
    col2 = np.random.normal(-2, 0.5, 100000)  # vector col2

#    print(np.shape(col1))
#    print(np.shape(col2))
#    print(col1, np.mean(col1), np.std(col1))
#    print(col2, np.mean(col2), np.std(col2))

    # stacks 1-D arrays as columns into a 2-D array
    return np.column_stack((col1, col2))


""" for testing purposes only
if __name__ == '__main__':
    X = assignment_03_01()
    print(X)
    X = assignment_03_02()
    print(X)
    npArr = np.ones((4, 5), dtype=int)
    assignment_03_03(npArr)
    res = assignment_03_04()

    print(np.shape(res), type(res))
"""
