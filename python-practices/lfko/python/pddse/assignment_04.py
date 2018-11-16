'''
Created on Nov 14, 2018

    solution for assignment_04

@author: fb
'''

import numpy as np
import pandas as pd

pd.set_option('display.max_columns', 500)


def assignment_04_01(df=pd.read_csv("data/zuwendungen-berlin.csv.gz")):
    """ 
    Params:
        loads a csv and returns 
            - the count
            - the mean
            - the standard deviation
            - the minimum
            - the 25% percentile
            - the 50% percentile (median)
            - the 75% percentile
            - the maximum
    Returns:
        DataFrame containing the above mentioned statistics
    
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError('no pandas DataFrame had been supplied!')
    spending_statistics = df['Betrag'].describe() # generates the beforementioned statistics

    return spending_statistics


def assignment_04_02(df=pd.read_csv("data/zuwendungen-berlin.csv.gz")):
    """ 
        Params: DataFrame created from a csv (or, if omitted, the default one will be used)
        Returns: a list of names which sum of 'Betrag' equals 143
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError('no pandas DataFrame had been supplied!')
    money_received = df.groupby(['Name'])['Betrag'].agg({'sum'})
    # retrieve only those names which sums are equal to 143
    names_of_recipients = money_received[money_received['sum'] == 143]
    # 'Name' now functions as an index, which is a list of identifier - extract them and return it
    return list([x for x in  names_of_recipients.index])


def assignment_04_03(df=pd.read_csv("data/zuwendungen-berlin.csv.gz")):
    """
        Params: DataFrame created from a csv (or, if omitted, the default one will be used)
        Returns: numpy array containing the values min, max and median
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError('no pandas DataFrame had been supplied!')
    # use the three aggregate functions on the column 'Betrag'
    spending_per_ressort = df.groupby(['Politikbereich'])['Betrag'].agg({'min', 'median', 'max'})
    # get all entries vor the index 'Wissenschaft'
    df = spending_per_ressort[spending_per_ressort.index.str.startswith('Wissenschaft')]
    
    # put min, max and median in a list - needs to be sorted before returning
    return np.sort(np.array([val for val in df.loc['Wissenschaft']]))


def assignment_04_04(df=pd.read_csv("data/zuwendungen-berlin.csv.gz")):
    """
        Params: DataFrame created from a csv (or, if omitted, the default one will be used)
        Returns: ordered list of U-Bahn-lines, order from most spendings to least spendings
    """
    
    if not isinstance(df, pd.DataFrame):
        raise ValueError('no pandas DataFrame had been supplied!')
    
    # df[(df.Politikbereich == 'Verkehr') & df.Zweck.str.extract('(U[1-9])')] -> MemoryError
    # select all those rows, where 'Bereich' == 'Verkehr' and which contain an U-Bahn-line occurrence
    df_ub = df[(df.Politikbereich == 'Verkehr') & df['Zweck'].str.contains('U[1-9]')]
    # now look for all occurences of U-Bahn-lines in the rows and list them per row
    df_ub['U-Bahn-Linie'] = df_ub['Zweck'].str.extract('(U[1-9])')
    # use the new column to group by and then aggregated via sum operation; order from highest to lowest
    df_ub_agg = df_ub.groupby(['U-Bahn-Linie'])['Betrag'].agg('sum').sort_values(ascending=False)
    
    return [ub for ub in df_ub_agg.index]

"""
if __name__ == '__main__':
    assignment_04_01()
    assignment_04_02()
    assignment_04_03()
    assignment_04_04()
"""    
