'''
Created on 25.09.2017

@author: fbecke12
'''

import scipy
import numpy as np
import matplotlib
import pandas as pd
import sklearn

from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression

# 25.09. quandl financial and economic datasets
import quandl, math

import os
from sklearn.decomposition.tests.test_nmf import random_state

os.environ['HTTP_PROXY']  = "http://10.175.249.97:8080"
os.environ['HTTPS_PROXY'] = "https://10.175.249.97:8080"

#get stock development of Google (no live data)
df = quandl.get("WIKI/GOOGL")

#shows some data 
#print(df.head())

# data needs to be formatted in order to be useful for our purpose
# the original data set has too many columns, thus making it difficult/more complex to apply a model
# that is why we select these already adjusted columns out of the data set. this ist what we will work with
df = df[['Adj. Open',  'Adj. High',  'Adj. Low',  'Adj. Close', 'Adj. Volume']]

print("adjusted data set: ")
print(df.head())


# high low percentage
# measures to some extent the volatility of the stock
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low']) / df['Adj. Low'] * 100.0

# daily percent change
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0

# put this all into a new dataframe
df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]
print("data set with new columns: ")
print(df.head())

# now let's get to some preprocessing for cleaning and further sampling of the data set
# this will make the prediction easier since data is in an appropriate format then
forecast_col = 'Adj. Close'
# fill none values with -99999
df.fillna(value=-99999, inplace=True)
forecast_out = int(math.ceil(0.01 * len(df)))
#print(forecast_out)

# the label we want to predict 
df['label'] = df[forecast_col].shift(-forecast_out)
#print('#####################')
#print(df.head(20))
#print(df.tail())



# the features - it is retrieved by dropping the column label of the dataframe
# we are creating two numpy arrays
X = np.array(df.drop(['label'], 1))
# the corresponding labels

X = preprocessing.scale(X)
X = X[:-forecast_out]
# drop any NaN values
df.dropna(inplace=True)

y = np.array(df['label'])
# split up the sample data using cross validation into training data and sample data for validating our test result
# test_size tells us the proportion of divisioning
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)

# now to the classifier - we use a support vector regression "classifier"
#clf = svm.SVR()
clf = LinearRegression()
# fit => train the model
clf.fit(X_train, y_train)
# and afterwards get a glimpse on the models confidence
confidence = clf.score(X_test, y_test)
print("scored confidence ")
print(confidence)

'''
for k in ['linear','poly','rbf','sigmoid']:
    clf = svm.SVR(kernel=k)
    clf.fit(X_train, y_train)
    confidence = clf.score(X_test, y_test)
    print(k,confidence)
'''