'''
    Created on Jan 13, 2019

    @author: fb
    @summary: Kaggle "Data Cleaning Challenge" (by Rachael Tatman (@rctatman))
'''

import numpy as np
import pandas as pd


def main():
    """
    
    """
    np.random.seed(0)
    df = loadData()  # load the San Francisco building permits list

    print(df.head(5))  # show first 10 rows
    # print(df.sample(5)) or randomly pick n rows
    print(df.keys())  # column name

    # NaNs and (presumably) missing values can be spotted; sum per column
    # sum_of_nas = df.isna().sum();
    sum_of_nulls = df.isnull().sum()
    # yields the same results
    
    # print(sum_of_nas)
    print(sum_of_nulls) 
    print(sum_of_nulls[0:10])

    print(ratioOfMissingVals(df))  # 26 % of the total values are actually missing or nulls or nans

    # btw lot of missing values in Street Number Suffix, bc. it was not recorded?
    # Zipcode also contains missing values
    
    df_dropped_nas = dropNAColums(df)
    print(df_dropped_nas.shape[1])  # how many columns are still there? -> 12 (before it was 43)
    print(' DataFrame after dropping colums: ', df_dropped_nas.isnull().sum())
    fillMissingVals(df_dropped_nas)
    
    print(df_dropped_nas.isnull().sum())
    
    print(ratioOfMissingVals(df_dropped_nas))


def ratioOfMissingVals(df):
    """
        @summary: calculates the ratio of missing values to the total amount of cells
        @return: ratio in percent
    """
    
    total_cells = np.product(df.shape) 
    total_sum_of_missing = df.isnull().sum().sum()
    
    ratio = (total_sum_of_missing / total_cells) * 100
    
    return ratio


def fillMissingVals(df):
    """
        @summary: E.g. by imputing the values from the existing ones
    """
    # at first impute row-wise, and afterwards fill the remaining cells with zeros
    df.fillna(method='bfill', axis=0).fillna(0)
    

def dropNAColums(df):
    """
        @summary: quick-and-dirty approach: remove columns, where at least one value is missing
    """
    df_dropped_nas = df.dropna(axis=1)
    
    return df_dropped_nas


def loadData():
    """
    
    """
    df = pd.read_csv('../../../data/Building_Permits.csv')
    
    return df
    

if __name__ == '__main__':
    main()
