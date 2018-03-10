'''
Created on Mar 9, 2018

@author: lfko
'''
import numpy as np
import datetime as dt

import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

# for reading csv files
import pandas as pd


def main():

    dataframe = pd.read_csv("clustering.csv")
    # define an index for our dataframe - for this, reuse the already contained StreckenID
    # with using inplace, the variable itself will be modified, so we do not need to reassign the dataframe to a new variable
    dataframe.set_index('StreckenID', inplace=True)
    print(dataframe.head(5))
    
    start = dt.datetime(2018, 3, 1)
    end = dt.datetime(2018, 3, 9)
    
    print(start)
    print(end)
    
    # plain python dictionary
    web_stats = {'Day':[1, 2, 3, 4, 5, 6],
                 'Visitors':[43, 34, 65, 56, 29, 76],
                 'Bounce Rate':[65, 67, 78, 65, 45, 52]}
    
    print(web_stats)
    # can be easily converted to a panda dataframe
    df = pd.DataFrame(web_stats)
    df.set_index('Day', inplace=True)
    print(df)
    
    # df['Visitors'].plot()
    # plt.show()
    dataframe = dataframe.rename(columns=lambda x: x.strip())
    print(dataframe.keys())
    # dataframe[['Laenge']].plot()
    # plt.show()
    printScatterPlot(dataframe)


def printScatterPlot(dataToPlot):
    
    ax1 = plt.scatter(dataToPlot['Laenge'], dataToPlot['MaxSteigung'], label='eins', color='r', s=25)
    ax2 = plt.scatter(dataToPlot['Laenge'], dataToPlot['Hoehenmeter'], label='zwei', color='g', s=25)
    ax3 = plt.scatter(dataToPlot['Laenge'], dataToPlot['AnteilSchotterwege'], label='drei', color='b')
    plt.xlabel('Laenge')
    # plt.ylabel('MaxSteigung')
    plt.title('Interesting Graph\nCheck it out')
    plt.legend()
    # plt.show()
    
    None;


if __name__ == "__main__":
    main() 
