'''
Created on Apr 8, 2019

@author: Florian "lfko" Becker
'''

import csv
import numpy as np
import operator
import matplotlib.pyplot as plt


def readDomain():
    '''
        @summary: read domain values, e.g. from a CSV
    '''
    y = []
    x = []
    z = []
    with open('domain_data.csv', 'r') as csv_file:
        filereader = csv.reader(csv_file, delimiter='\t')
        for row in filereader:
            y.append(row[0])
            x.append(row[1])
            z.append(row[3])

    # myZip = zip(x, y, Z)

    # xx = np.ravel(x); yy = np.ravel(y) ; zz = np.ravel(z)

    plt.clf()
    # plt.contourf(x, y, z)
    plt.scatter(x, y, c=z)
    plt.plot(x[0:2], y[0:2], 'ro-')
    plt.plot(x[1:3], y[1:3], 'ro-')
    plt.plot([x[2:3], x[0:1]], [y[2:3], y[0:1]], 'ro-')    

    # plt.plot(y[0], '+r')  # first/base point
    
    print(buildSimplex((x[0], y[0]), (x[1], y[1]), (x[2], y[2]), z[0], z[1], z[2]))
    plt.show()
     
    # X, Y = np.meshgrid(x, y)

                
def buildSimplex(A, B, C, fA, fB, fC):
    '''
        @param A: coordinates for point A
        @param B: coordinates for point B
        @param C: coordinates for point C
        @param fA: value for point A
        @param fB: value for point B
        @param fC: value for point C
    '''
    return [(A, fA), (B, fB), (C, fC)]


if __name__ == '__main__':
    '''
    '''
    bestSimplex = []
    readDomain()
