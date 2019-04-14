'''
'''
import csv
import numpy as np
import operator
import matplotlib.pyplot as plt
from matplotlib.mlab import griddata
'''
    mathematical functions
'''


def f(x, y):
    '''
        @summary: the function we'd like to optimize/use for evaluation
        @param points: 
    '''
    return ((x ** 2 + y - 11) ** 2) + ((x + y ** 2 - 7) ** 2)
    # return x ** 2 - 4 * x + y ** 2 - y - x * y

'''
    miscellaneous
'''


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
    
    plt.show()
     
    # X, Y = np.meshgrid(x, y)
                
    return X, Y, Z


def genDomain(start=-5, end=5):
    '''
        @summary: generate domain
    '''
    x = np.linspace(start, end, 1000)
    y = np.linspace(start, end, 1000)
    
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)
    print(Z)

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
    T = [(simplex[i], funcVals[i]) for i in range(len(simplex))] 
    # sort the list ascending using the second tuple element (function value) 
    # BS.sort(key=operator.itemgetter(1))
    return sorted(T, key=operator.itemgetter(1))


def updateBestSimplex(A, B, C, func):
    '''
    '''
    sm = [A, B, C]  # get new coordinates
    sm_eval = evaluate(func, sm)  # calculate function values
    return fitBestSimplex(sm, sm_eval)  # return new simplex with ordered points


def initSimplex(dim, step=0.3, start=-5, stop=5):
    '''
        @summary: constructs an initial simplex in the given dimension
        @param dim: dimension
        @param step: randomization factor
    '''
    # initial values
    x_p = 0.0
    y_p = 0.0
    return [(x_p + (step * i * np.random.randint(start, stop)), y_p + (step * i * np.random.randint(start, stop))) for i in range(dim)]

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
    return (2. * m[0] - WP[0], 2. * m[1] - WP[1])
    # return m + alpha * (m - x_h)


def doExpansion(m, RP, gamma=2):
    '''
        @param m: midpoint
        @param x_h: worst point
        @param gamma: expansion parameter
        @return: expanded point
    '''
    return ((2. * RP[0] - m[0], 2. * RP[1] - m[1]))


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


def calcCentroid(BS, P_1=0, P_2=1):
    '''
        @summary: 
        @param BS: current BestSimplex
        @return: midpoint between best and good point
    '''
    
    # compute the sum divided by the number of points
    return ((BS[P_1][0][0] + BS[P_2][0][0]) / 2., (BS[P_1][0][1] + BS[P_2][0][1]) / 2.)


def optimize(BS, iterate=15):
    '''
        @summary: the actual optimization
    '''
    
    print("k \t {:^10}   \t {:^25}   \t {:^15}".format("Best point", "Good point", "Worst point"))
    
    for _ in range(iterate):
        m = calcCentroid(BS) 
        WP = BS[dim][0]  # worst point coordinates
        GP = BS[1][0]  # good point coordinates
        BP = BS[0][0]  # best point coordinates
        
        print("{} \t f({:.2f},{:.2f})   \t f({:.2f},{:.2f})   \t f({:.2f},{:.2f})"
                .format(_ + 1, BS[0][0][0], BS[0][0][1],
                        BS[1][0][0], BS[1][0][1], BS[2][0][0], BS[2][0][1]))
        
        RP = doReflection(m, WP)  # reflection point
        fRP = f(RP[0], RP[1]) 
        # (1) check if reflection point is better (with regard to f(x, y)) than the good point function value
        if  fRP < BS[1][1]:
            print('case (I)')
            if BS[0][1] < fRP:
                BS = updateBestSimplex(BP, GP, RP, f)
                # print('new BestSimplex: ', BS)
            else:    
                EP = doExpansion(m, RP)  # expansion point
                
                if fRP < BS[0][1]:
                    BS = updateBestSimplex(BP, GP, EP, f)
                else:
                    BS = updateBestSimplex(BP, GP, RP, f)
    
                # print('new BestSimplex: ', BS)
        
        else:
            print('case (II)')
            if fRP < BS[dim][1]:
                BS = updateBestSimplex(BP, GP, RP, f)
            
            CP = doContraction(m, BS)  # contraction point
            if f(CP[0], CP[1]) < BS[dim][1]:
                BS = updateBestSimplex(BP, GP, CP, f)
            else:
                m, CPP = doCompression(BS)
                BS = updateBestSimplex(BP, m, CPP, f)
            
        plotFunc(BS)
        
        print('end of iteration #', _, ' - new BS: ', BS)
        
    print('final Simplex: ', BS)
    plt.show()


def plotFunc(simplex):
    '''
        @summary: plot the function
    '''
    bgw = np.array([simplex[i][0] for i in range(len(simplex))])
    plt.clf()
    plt.contourf(X, Y, Z)
    plt.plot((bgw[0, 0], bgw[1, 0]), (bgw[0, 1], bgw[1, 1]), '-c')
    plt.plot((bgw[2, 0], bgw[1, 0]), (bgw[2, 1], bgw[1, 1]), '-c')
    plt.plot((bgw[0, 0], bgw[2, 0]), (bgw[0, 1], bgw[2, 1]), '-c')
    plt.plot(bgw[0, 0], bgw[0, 1], '+r')  # first/base point
    plt.show(block=False)
    plt.pause(0.1)


def plotDomain():
    '''
        @summary: plot the domain (without simplex)
    '''
    plt.clf()
    plt.contourf(X, Y, Z)
    plt.show()

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
    bsm = fitBestSimplex(sm, sm_eval)
    
    # (4) generate domain for plotting and optimization
    X, Y, Z = genDomain()
    # plotFunc()
    # print(BS)
    # X, Y, Z = readDomain()
    # plotDomain()
    optimize(bsm, iterate=15)
