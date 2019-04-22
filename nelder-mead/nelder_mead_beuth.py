'''
Created on Apr 8, 2019

@author: Florian "lfko" Becker
'''

import tkinter as tk
import csv
import numpy as np
import operator
import matplotlib.pyplot as plt


class nelderMead():

    def readDomain(self):
        '''
            @summary: read domain values, e.g. from a CSV
        '''
        y = []
        x = []
        z = []
        with open('domain_data.csv', 'r') as csv_file:
            filereader = csv.reader(csv_file, delimiter=',')
            for row in filereader:
                y.append(float(row[0]))
                x.append(float(row[1]))
                z.append(float(row[3]))
                setNum = int(row[4])
                self.points.append(((float(row[1]), float(row[0])), float(row[3]), setNum))
    
        return y, x, z
    
    def plotSimplex(self, simplex):
        '''
            @summary: plots the current simplex
        '''
        bgw = np.array([simplex[i][0] for i in range(len(simplex))])
        plt.clf()
        plt.scatter(self.X, self.Y, c=self.Z)
        plt.plot((bgw[0, 0], bgw[1, 0]), (bgw[0, 1], bgw[1, 1]), '-c')
        plt.plot((bgw[2, 0], bgw[1, 0]), (bgw[2, 1], bgw[1, 1]), '-c')
        plt.plot((bgw[0, 0], bgw[2, 0]), (bgw[0, 1], bgw[2, 1]), '-c')
        plt.plot(bgw[0, 0], bgw[0, 1], '+r')  # first/base point 
        plt.show()
    
    def readNextSimplex(self, k):
        '''
            @param k: kth iteration
        '''
        A, B, C = self.points[k * 3:k * 3 + 3]
        
        return self.buildSimplex(A[0], B[0], C[0], A[1], B[1], C[1])
                    
    def buildSimplex(self, A, B, C, fA, fB, fC):
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
    
    def doReflection(self, CP, WP):
        '''
            @param CP: centroid point
            @param WP: worst point
            @return: reflected point
        '''
        return ((2. * CP[0]) - WP[0], (2. * CP[1]) - WP[1])
    
    def doExpansion(self, CP, RP, gamma=2):
        '''
            @param CP: midpoint
            @param RP: reflection point
            @param gamma: expansion parameter
            @return: expanded point
        '''
        return ((2. * RP[0]) - CP[0], (2. * RP[1]) - CP[1])
    
    def doContraction(self, CP, WP):
        '''
            @param points: points, worst one excluded
            @param x_h: worst point
            @param beta: contraction parameter
            @return: contracted point
        '''    
        
        # m = calcCentroid(BS)
        RP = self.doReflection(CP, WP)
        C1P = ((RP[0] + CP[0]) / 2., (RP[1] + CP[1]) / 2.)
        C2P = ((WP[0] + CP[0]) / 2., (WP[1] + CP[1]) / 2.)
        if self.getValueForPoint(C1P) <= self.getValueForPoint(C2P):
            return C1P
        return C2P
    
    def doCompression(self, BS):
        '''
            @summary: nelder-mead compression
            @param BS: current BestSimplex
        '''
        return self.calcCentroid(BS), self.calcCentroid(BS, P_1=0, P_2=2)
    
    def calcCentroid(self, BP, GP, P_1=0, P_2=1):
        '''
            @summary: 
            @param BS: current BestSimplex
            @return: midpoint between best and good point
        '''
        # compute the sum divided by the number of points
        return ((BP[0] + GP[0]) / 2., (BP[1] + GP[1]) / 2.)
    
    def optimize(self, iterate=15):
        '''
            @summary: the actual optimization
        '''
        
        print("k \t {:^10}   \t {:^40}   \t {:^20}".format("Best point", "Good point", "Worst point"))
        
        for k in range(iterate):
            BS = self.readNextSimplex(k)
            # m = calcCentroid(BS) 
            WP = BS[self.dim][0]  # worst point coordinates
            GP = BS[1][0]  # good point coordinates
            BP = BS[0][0]  # best point coordinates
            
            fWP = BS[self.dim][1]
            fGP = BS[1][1]
            fBP = BS[0][1]
            
            print("{} \t {}({})   \t {}({})   \t {}({})"
                    .format(k + 1, BS[0][0], fBP, BS[1][0], fGP, BS[self.dim][0], fWP))
            
            CP = self.calcCentroid(BP, GP) 
            RP = self.doReflection(CP, WP)  # reflection point
            fRP = self.getValueForPoint(RP)
            
            print("Reflection point: {}({})".format(RP, fRP))
    
            EP = self.doExpansion(CP, RP)  # extend the reflected point
            fEP = self.getValueForPoint(EP)
                
            print("Expansion point: {}({})".format(EP, fEP))
    
            if fEP == None:
                fEP = 0.0
            if fRP == None:
                fRP = 99.9
    
            if fRP < fGP:
                print('case (I)')
    
                # BS = buildSimplex(BP, GP, RP, fBP, fGP, fRP)  # WP -> RP
                print('use the Reflection Point and substitute the Worst Point with it')
    
            elif fRP < fBP:
                print('case (II)')
                
                EP = self.doExpansion(CP, RP)  # extend the reflected point
                fEP = self.getValueForPoint(EP)
                
                print("Expansion point: {}({})".format(EP, fEP))
                
                if fEP < fRP:
                    # BS = buildSimplex(BP, GP, EP, fBP, fGP, fEP)  # WP -> EP
                    print('use the Expansion Point and substitute the Worst Point with it')
                else:
                    # BS = buildSimplex(BP, GP, RP, fBP, fGP, fRP)  # WP -> RP
                    print('use the Reflection Point and substitute the Worst Point with it')
                    
            else:
                print('inequalities are not satisfied')
                CP = self.doContraction(CP, WP)
                fCP = self.getValueForPoint(CP)
                
                print("Contraction point: {}({})".format(CP, fCP))
                
                if fCP < fGP:
                    # BS = buildSimplex(BP, GP, CP, fBP, fGP, fCP)  # WP -> CP
                    print('use the Contraction Point and substitute the Worst Point with it')
                else:
                    print('shrink')
                    
                    # BS = buildSimplex(BP, GP, CP, fBP, fGP, fCP)  # WP -> CP
                    # print('new BestSimplex: ', BS)
                    
        print('final Simplex: ', BS)
        plt.show()
    
    def getValueForPoint(self, pt):
        '''
        '''
        for point in self.points:
            if pt in point:
                return point[1]

    def initGUI(self):
        '''
        '''
        w, h = 300, 200
        window = tk.Tk()
        window.title("A figure in a canvas")
        canvas = tk.Canvas(window, width=w, height=h)
        canvas.pack()

    def __init__(self, root):
        '''
        '''
        
        self.initGUI()
        
        self.points = []
        self.dim = 2
        self.Y, self.X, self.Z = self.readDomain()
    
        # BS = readNextSimplex(0)
        # BS = buildSimplex((X[0], Y[0]), (X[1], Y[1]), (X[2], Y[2]), Z[0], Z[1], Z[2])
        # print(bestSimplex)
        # plotSimplex(bestSimplex)
        
        self.optimize(15)

    
# root window widget - must be generated before anything else
root = tk.Tk()
root.geometry("400x300")
mainGui = nelderMead(root)

# starts the actual execution
# mainloop will be executed indefinetly long, until we close the window
root.mainloop()
