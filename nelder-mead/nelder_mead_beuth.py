'''
Created on Apr 8, 2019

@author: Florian "lfko" Becker
'''

import csv
import numpy as np
import operator
import matplotlib.pyplot as plt
from distutils.command.build import build


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
            y.append(float(row[0]))
            x.append(float(row[1]))
            z.append(float(row[3]))
            points.append(((float(row[1]), float(row[0])), float(row[3])))

    return y, x, z


def plotSimplex(simplex):
    '''
        @summary: plots the current simplex
    '''
    bgw = np.array([simplex[i][0] for i in range(len(simplex))])
    plt.clf()
    plt.scatter(X, Y, c=Z)
    plt.plot((bgw[0, 0], bgw[1, 0]), (bgw[0, 1], bgw[1, 1]), '-c')
    plt.plot((bgw[2, 0], bgw[1, 0]), (bgw[2, 1], bgw[1, 1]), '-c')
    plt.plot((bgw[0, 0], bgw[2, 0]), (bgw[0, 1], bgw[2, 1]), '-c')
    plt.plot(bgw[0, 0], bgw[0, 1], '+r')  # first/base point 
    plt.show()
    
                
def buildSimplex(A, B, C, fA, fB, fC):
    '''
        @param A: coordinates for point A
        @param B: coordinates for point B
        @param C: coordinates for point C
        @param fA: value for point A
        @param fB: value for point B
        @param fC: value for point C
        @return: ordered simplex: Best Point, Good Point, Worst Point
    '''
    return sorted([(A, fA), (B, fB), (C, fC)], key=operator.itemgetter(1))

"""
    Nelder-Mead functions
"""


def doReflection(CP, WP, alpha=1):
    '''
        @param m: midpoint
        @param WP: worst point
        @param alpha: reflection parameter
        @return: reflected point
    '''
    # return (CP[0] - alpha * WP[0], CP[1] - alpha * WP[1])
    return (2. * CP[0] - WP[0], 2. * CP[1] - WP[1])


def doExpansion(CP, RP, gamma=2):
    '''
        @param CP: midpoint
        @param RP: reflection point
        @param gamma: expansion parameter
        @return: expanded point
    '''
    return (2. * RP[0] - CP[0], 2. * RP[1] - CP[1])


def doContraction(m, BS):
    '''
        @param points: points, worst one excluded
        @param x_h: worst point
        @param beta: contraction parameter
        @return: contracted point
    '''    
    
    # m = calcCentroid(BS)
    RP = doReflection(m, BS[dim][0])
    WP = BS[2][0]
    C1P = ((RP[0] + m[0]) / 2., (RP[1] + m[1]) / 2.)
    C2P = ((WP[0] + m[0]) / 2., (WP[1] + m[1]) / 2.)
    if f(C1P[0], C1P[1]) <= f(C2P[0], C2P[1]):
        return C1P
    return C2P


def doCompression(BS):
    '''
        @summary: nelder-mead compression
        @param BS: current BestSimplex
    '''
    return calcCentroid(BS), calcCentroid(BS, P_1=0, P_2=2)


def calcCentroid(BP, GP, P_1=0, P_2=1):
    '''
        @summary: 
        @param BS: current BestSimplex
        @return: midpoint between best and good point
    '''
    # compute the sum divided by the number of points
    return ((BP[0] + GP[0]) / 2., (BP[1] + GP[1]) / 2.)


def optimize(BS, iterate=15):
    '''
        @summary: the actual optimization
    '''
    
    print("k \t {:^10}   \t {:^10}   \t {:^10}".format("Best point", "Good point", "Worst point"))
    
    for _ in range(iterate):
        # m = calcCentroid(BS) 
        WP = BS[dim][0]  # worst point coordinates
        GP = BS[1][0]  # good point coordinates
        BP = BS[0][0]  # best point coordinates
        
        print("{} \t {}   \t {}   \t {}"
                .format(_ + 1, BS[0][0], BS[1][0], BS[dim][0]))
        
        CP = calcCentroid(BP, GP) 
        RP = doReflection(CP, WP)  # reflection point
        print('RP: ', RP)
        print(getValueForPoint(RP), getValueForPoint(GP))
        if  getValueForPoint(RP) < getValueForPoint(GP):
            print('case (I)')
            print(getValueForPoint(RP), getValueForPoint(BP))
            if getValueForPoint(BP) > getValueForPoint(RP):
                BS = buildSimplex(BP, GP, RP, getValueForPoint(BP), getValueForPoint(GP), getValueForPoint(RP))
                print('new BestSimplex: ', BS)
            
            else:    
                EP = doExpansion(CP, RP)  # expansion point
                print('EP ', EP)
                print(getValueForPoint(EP))

                if getValueForPoint(RP) < getValueForPoint(BP):
                    BS = buildSimplex(BP, GP, EP, getValueForPoint(BP), getValueForPoint(GP), getValueForPoint(EP))
                else:
                    BS = buildSimplex(BP, GP, RP, getValueForPoint(BP), getValueForPoint(GP), getValueForPoint(RP))
    
                print('new BestSimplex: ', BS)
        
    print('final Simplex: ', BS)
    plt.show()


def getValueForPoint(pt):
    '''
    '''
    for point in points:
        if pt in point:
            return point[1]


if __name__ == '__main__':
    '''
    '''
    points = []
    dim = 2
    Y, X, Z = readDomain()
    bestSimplex = buildSimplex((X[0], Y[0]), (X[1], Y[1]), (X[2], Y[2]), Z[0], Z[1], Z[2])
    # plotSimplex(bestSimplex)
    
    optimize(bestSimplex, 5)
    
