'''
'''

import numpy as np
import operator
import matplotlib.pyplot as plt
'''
    mathematical functions
'''


def f(x, y):
    '''
        @summary: the function we'd like to optimize/use for evaluation
        @param points: 
    '''
    return ((x ** 2 + y - 11) ** 2) + ((x + y ** 2 - 7) ** 2)

'''
    miscellaneous
'''


def genDomain():
    '''
        @summary: generate domain
    '''
    x = np.linspace(-4, 4, 1000)
    y = np.linspace(-4, 4, 1000)
    
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)

    return X, Y, Z

'''
    simplex functions
'''


def evaluate(func, simplex):
    '''
        @param func: function to use for evaluation
        @param simplex: simplex we'd like to evaluate for further optimization
    '''
    return [func(simplex[i][0], simplex[i][1]) for i in range(len(simplex))]
    

def fitBestSimplex(simplex, funcVals):
    '''
        @summary: evaluate best current simplex by sorting points with regard to their function values
        @param simplex: current simplex (only coordinates)
        @param funcVals: respective function values
        @return: BS - (sorted) BestSimplex
    '''
    # tuple inside a tuple
    BS = [(simplex[i], funcVals[i]) for i in range(len(simplex))] 
    # sort the list ascending using the second tuple element (function value) 
    # BS.sort(key=operator.itemgetter(1))
    return sorted(BS, key=operator.itemgetter(1))


def updateBestSimplex(A, B, C, func):
    '''
    '''
    sm = [A, B, C]
    sm_eval = evaluate(func, sm)
    return fitBestSimplex(sm, sm_eval)


def initSimplex(dim, step=0.3):
    '''
        @summary: constructs an initial simplex in the given dimension
        @param dim: dimension
        @param step: randomization factor
    '''
    # initial values
    x_p = 0.0
    y_p = 0.0
    return [(x_p + (step * i * np.random.randint(-4, 4)), y_p + (step * i * np.random.randint(-4, 4))) for i in range(dim)]

'''
    nelder-mead algorithm
'''


def doReflection(m, WP, alpha=1):
    '''
        @param m: midpoint
        @param WP: worst point
        @param alpha: reflection parameter
        @return: reflected point
    '''
    return ((2 * m[0] - WP[0], 2 * m[1] - WP[1]))
    # return m + alpha * (m - x_h)


def doExpansion(m, RP, gamma=2):
    '''
        @param m: midpoint
        @param x_h: worst point
        @param gamma: expansion parameter
        @return: expanded point
    '''
    return ((2 * RP[0] - m[0], 2 * RP[1] - m[1]))


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


def doCompression(BS, BP, WP, delta=0.5):
    '''
        @param points: points, worst one excluded
        @param x_s: 2nd worst point
        @param x_h: worst point
        @param x_l: best point
        @param delta: compression parameter
    '''
    return calcCentroid(BS), calcCentroid(BS, P_1=0, P_2=2)


def calcCentroid(simplex, P_1=0, P_2=1):
    '''
        @param simplex: current simplex
        @return: midpoint between best and good point
    '''
    
    # compute the sum divided by the number of points
    return ((simplex[P_1][0][0] - simplex[P_2][0][0]) / 2, (simplex[P_1][0][1] - simplex[P_2][0][1]) / 2)


def optimize(BS, iter=15):
    '''
        @summary: the actual optimization
    '''
    for _ in range(iter):
        m = calcCentroid(BS) 
        WP = BS[dim][0]  # worst point
        GP = BS[1][0]  # good point
        BP = BS[0][0]  # best point
        RP = doReflection(m, WP)  # reflection point
        
        # (1) check if reflection point is better (with regard to f(x, y)) than the good point
        if f(RP[0], RP[1]) < f(GP[0], GP[1]):
            print('case (I)')
            if f(BP[0], BP[1]) < f(RP[0], RP[1]):
                BS = updateBestSimplex(BP, GP, RP, f)
                print('new BestSimplex: ', BS)
            else:    
                EP = doExpansion(m, RP)  # expansion point
                
                if f(EP[0], EP[1]) < f(BP[0], BP[1]):
                    BS = updateBestSimplex(BP, GP, EP, f)
                else:
                    BS = updateBestSimplex(BP, GP, RP, f)
    
                print('new BestSimplex: ', BS)
        
        else:
            print('case (II)')
            if f(RP[0], RP[1]) < f(WP[0], WP[1]):
                BS = updateBestSimplex(BP, GP, RP, f)
            
            CP = doContraction(m, BS)  # contraction point
            if f(CP[0], CP[1]) < f(WP[0], WP[1]):
                BS = updateBestSimplex(BP, GP, CP, f)
            else:
                m, CPP = doCompression(BS, BP, WP)
                BS = updateBestSimplex(BP, m, CPP, f)
                
            print('new BestSimplex: ', BS)
        
        plotFunc(BS)


def plotFunc(simplex):
    '''
        @summary: plot the function
    '''
    bgw = np.array([simplex[i][0] for i in range(len(simplex))])
    plt.clf()
    plt.contour(X, Y, Z)
    plt.plot((bgw[0, 0], bgw[1, 0]), (bgw[0, 1], bgw[1, 1]), '-c')
    plt.plot((bgw[2, 0], bgw[1, 0]), (bgw[2, 1], bgw[1, 1]), '-c')
    plt.plot((bgw[0, 0], bgw[2, 0]), (bgw[0, 1], bgw[2, 1]), '-c')
    plt.plot(bgw[0, 0], bgw[0, 1], '.r')
    plt.show(block=False)
    plt.pause(0.1)

'''
    main
'''

if __name__ == '__main__':
    '''
        @summary: main function
    '''
    dim = 2
    # (1) create initial simplex
    sm = initSimplex(3, 0.3)
    # (2) eval the simplex with regard to the function
    sm_eval = evaluate(f, sm)
    # (3) sort the points using the value of the function
    BS = fitBestSimplex(sm, sm_eval)

    # (4) generate domain for plotting and optimization
    X, Y, Z = genDomain()
    # plotFunc()
    print(BS)

    optimize(BS)
