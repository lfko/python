'''
Created on 21.09.2017

machine learning tutorial
dataset: iris flower set

@author: fbecke12
'''

'''
first of all we need to import all of the needed libraries
'''

import sys
print('Python version: {}'.format(sys.version))

import scipy
print('scipy version: {}'.format(scipy.__version__))

import numpy
print('numpy version: {}'.format(numpy.__version__))

import matplotlib
print('matplotlib: {}'.format(matplotlib.__version__))

import pandas
print('pandas: {}'.format(pandas.__version__))

import sklearn
print('sklearn: {}'.format(sklearn.__version__))

'''
now for a more refined import - all of the needed tools and special functions
'''
#TODO this one cannot be resolved. Why?
#from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC


'''
get hold of the data, i.e. load it into the applications context
'''
#uri to the dataset file
data_csv = "C:\Entwicklung\Projekte\lfko-ws\machine-learner\lfko\machine\learning\iris.data"
#the names of the different attributes of a row
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
#load the data into the workspace
dataset = pandas.read_csv(data_csv, names=names)

'''
now that the data has been loaded, we want to introspect it - for further analyzing the set
'''
#shape allows for a quick overview of the size of the dataset: how many indexes (i.e. number of rows, instances) and the number of columns
print('getting the datasets shape: '.format(dataset.shape))

print('an arbitrar extract of the first 20 rows: ')
print(dataset.head(20))

'''
show some statistical proportions of the dataset
'''
#is this showing the arithmetic mean?
print(dataset.describe())

'''
 ... and disitribution of the classes
'''
#they are equally distributed (1/3 per each class)
print(dataset.groupby('class').size())

'''
now for some visualisation
'''
#this creates an univariate plot, showing one plot per variable/parameter - since there are only four of them in the dataset
#this is sufficient here
#dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
#dataset.hist()
#plt.show()

'''
now to the actual work - we will use cross-validation (k-fold) for evaluating the model accuracy
'''
# Split-out validation dataset
array = dataset.values
# array filled with all the x variables, which means: all the parameter values
X = array[:,0:4]
# array with all y values, which means: all assigned classes
Y = array[:,4]
#print(X)
#print(Y)
#percentage - count of values, which will be used as test sample (and the residual 80% will be used for training the model)
validation_size = 0.20
# random seed
seed = 7
# split the dataset for our k-fold-cross-validation into four parts: x/y training and x/y validation
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)

# Test options and evaluation metric
seed = 7
#accuracy scoring means, that the ratio of right classified instance to the overall sum of instances is calculated; based on this
#an accuracy score can be calculated
scoring = 'accuracy'

# Spot Check Algorithms
models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
#non linear classifiers
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
#support vector machine
models.append(('SVM', SVC()))
# evaluate each model in turn
results = []
names = []
for name, model in models:
    #divide the data set into k different subsets, of which one will be the validation set and k-1 sets are for training purpose
    #by passing the same seed every time, we make so sure to always split up the data set in the same order, so we can asasure 
    #reproducable results
    kfold = model_selection.KFold(n_splits=10, random_state=seed)
    #cross validation score for the selected modeliui8888888i
    cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
    results.append(cv_results)
    names.append(name)
    msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
    print(msg)


# Compare Algorithms
fig = plt.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
plt.show()    
'''
now that we got the idea of the accuracies, we might pick out the one algorithm, which yields the best results
let's take a deeper look into the SVM-ML-algorithm, because it was the most accurate
''' 
knn = KNeighborsClassifier()       
svm = SVC()

svm.fit(X_train, Y_train)
#knn.fit(X_train, Y_train)
#final test: test it on the validation sample
predictions = svm.predict(X_validation)  
print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions))
    