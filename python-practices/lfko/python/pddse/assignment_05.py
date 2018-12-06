'''
Created on Nov 28, 2018

    solutions for assignment 05

@author: fb
'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# plt.style.use('bmh')


def assignment_05_01():
    """ plot some lines, starting and ending at given coordinates """
    plt.plot([-1, 3], [4, 5], 'r-x')
    plt.plot([1, 3], [8, 6], 'k-o')
    plt.xlabel("x axis")
    plt.ylabel("y axis")
    plt.show()  # finally, show the plot
    # plt.savefig("assignment_05_01.png")


def assignment_05_02():
    """ plots the data set 'dino' """
    df = pd.read_csv("data/DatasaurusDozen.tsv", sep='\t')
    # extract data belonging to the dataset 'dino'
    dino_data = df[df['dataset'].str.contains('dino')]
    # star_data = df[df['dataset'].str.contains('star')]

    plt.figure(figsize=[10, 10])  # size of plot area
    plt.yticks([])
    plt.xticks([])
    # scatter plot: the data points will not be connected
    plt.plot(dino_data.x, dino_data.y, 'o', color='blue')
    plt.title('Datasaurus')
    plt.show()
    # plt.savefig("assignment_05_02.png")


def assignment_05_03():
    """ plots a histogram of normally distributed values (mean=5, sd=2)"""

    # create a normal distribution
    nd_var = pd.DataFrame(np.random.normal(5, 2, 1000))
    nd_var.plot.hist(grid=True, bins=20, rwidth=0.9, color='#607c8e')
    plt.title('Histogram of normal distribution')
    plt.xlabel('normal distribution data')
    plt.show()
    # plt.savefig("assignment_05_03.png")


def assignment_05_04():
    """ plots the joint kernel density estimate of a multivariate normal distribution """

    mean = [0, 0]
    cov = [[5, 2], [2, 2]]
    data = np.random.multivariate_normal(mean, cov, 1000)
    normal_data = pd.DataFrame(data, columns=['x', 'y'])

    sns.jointplot("x", "y", normal_data, kind='kde')
    plt.show()  # this call is mandatory, even when using seaborn
    # plt.savefig("assignment_05_04.png")


"""     
if __name__ == '__main__':
    assignment_05_01()
    assignment_05_02()
    assignment_05_03()
    assignment_05_01()
"""
