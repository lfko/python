'''
Created on 26.09.2017

STA203 - Seite 13

@author: fbecke12
'''

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

import matplotlib.pyplot as plt

# declare a dataset
# body heigth (in cm) and body weigth (in kg)
# n = 10
# (1) load the dataset into the workspace
data_uri = "/home/lfko/lfko-space/machine-learner/lfko/machine/learning/models/examples/regression/data.csv"
# provide names for the columns
names = ['heigth', 'weigth']
dataset = pd.read_csv(data_uri, names=names)

# exclude the weight column out of the frame - so we can have our single feature in an numpy array
X = np.array(dataset.drop(['weigth'], 1))
y = np.array(dataset['weigth'])

model = LinearRegression()
model.fit(X, y)

coefs = model.coef_
print("coefficient beta %s", coefs)
print("intercept b %s", model.intercept_)

X_predict = np.array([100000])
X_predict = X_predict.reshape(-1, 1)

prediction = model.predict(X_predict)
print(prediction)
