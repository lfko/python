'''
Created on 29.09.2017

python sample on linear multivariate regression

this examples uses some of the data from the diabetes set

@author: fbecke12
'''
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import matplotlib.pyplot as plt

# load the data
# the data set contains almost 500 entries with 10 features
diabetes = datasets.load_diabetes()

# extracts the second column of the data set - i.e. we are using only one future on the feature set
diab_X = diabetes.data[:, np.newaxis, 2]

# Split the data into training/testing sets
# from the beginning to the 19th index '-' means exclude that one
diab_X_train = diab_X[:-20]
diab_X_test = diab_X[-20:]

# Split the targets into training/testing sets
diab_y_train = diabetes.target[:-20]
diab_y_test = diabetes.target[-20:]

# for our model we will use linear regression
model = linear_model.LinearRegression()

# first of all: train the model, supplement it with the training data
model.fit(diab_X_train, diab_y_train)

# this contains the predicted data - afterwards we compar it with the actual test results to get our confidence score and error measurement
diab_y_pred = model.predict(diab_X_test)

# The coefficients
print('Coefficients: \n', model.coef_)
# The mean squared error
print("Mean squared error: %.2f"
      % mean_squared_error(diab_y_test, diab_y_pred))
# Explained variance score: 1 is perfect prediction
# Bestimmtheitsmass
print('Variance score: %.2f' % r2_score(diab_y_test, diab_y_pred))

# Plot outputs
plt.scatter(diab_X_test, diab_y_test,  color='black')
plt.plot(diab_X_test, diab_y_pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()