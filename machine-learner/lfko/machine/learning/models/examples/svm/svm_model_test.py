'''
Created on 24.09.2017

@author: fbecke12
'''
# TODO 24.09. 
# How can I handle the imports, this means how can I import the same libraries in multiple python modules?
import scipy
import numpy
import matplotlib
import pandas
import sklearn

# support vector machine model
from sklearn import svm

# different plotting functions
import matplotlib.pyplot as plt

# (1) load the dataset into the workspace
data_uri = "C:\Entwicklung\Projekte\lfko-ws\machine-learner\lfko\machine\learning\iris.data"
# provide names for the columns
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(data_uri, names=names)

# (2) plot the loaded data to get some better understanding via visualization
# TODO 24.09. try some of the different kinds of plots
dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
dataset.hist()
plt.show()