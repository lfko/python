'''
    Created on Jan 17, 2019

    @author: fb
    @summary: Just some random snippets regarding cross-validation and hyperparameter optimization
'''

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble.forest import RandomForestRegressor
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score, train_test_split, RandomizedSearchCV
from sklearn.neighbors import KNeighborsClassifier

import matplotlib.pyplot as plt 
import numpy as np

# Load the dataset
iris = load_iris()
X_iris = iris.data
y_iris = iris.target

# split the data into separate training and test data
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.33, random_state=42)

print(X_train)
print(X_test)

# Some nonlinear model
# model = KNeighborsClassifier(n_neighbors=3) # our non-linear model -> 0.98 accuracy
# model = KNeighborsClassifier(n_neighbors=2) # same
model = KNeighborsClassifier(n_neighbors=5)  # same
model.fit(X_train, y_train)

# predict the response
pred = model.predict(X_test)

# evaluate accuracy
print(accuracy_score(y_test, pred))  # 0.98 acc

# by supplying cv = 10 cross_val_score automatically will fold the train and test data 10 times
scores = cross_val_score(model, iris.data, iris.target, cv=10, error_score='accuracy')
print(scores)
print(' Mean: ', scores.mean())

# now trying to optimize it - we try different numbers of neighbours
n_neighbors = range(1, 30)
mean_scores = []

for n in n_neighbors:
    model = KNeighborsClassifier(n_neighbors=n)  # same
    model.fit(X_train, y_train)
    
    # predict the response
    pred = model.predict(X_test)
    
    # evaluate accuracy
    # print(accuracy_score(y_test, pred)) # 0.98 acc
    
    # by supplying cv = 10 cross_val_score automatically will fold the train and test data 10 times
    scores = cross_val_score(model, iris.data, iris.target, cv=10, error_score='accuracy')
    mean_scores.append(scores.mean())
    
plt.plot(n_neighbors, mean_scores)  # increases up to rougly 98 % between 12 and 17 neighbors; deteriorates with more neighours
# plt.show()

# now let us use a RandomForestClassifier
clf = RandomForestClassifier(n_jobs=2, random_state=0)
clf.fit(X_train, y_train)
pred = clf.predict(X_test)
scores = cross_val_score(model, iris.data, iris.target, cv=10, error_score='accuracy')
print(scores.mean())  # approx. 0.95 
# print(clf.get_params()) shows a lot of possible parameters for the RandomForestClassifier - we pick some to 'improve' the matching
rf = RandomForestClassifier()
# rf = RandomForestRegressor()
random_grid = {'n_estimators':[int(x) for x in np.linspace(100, 1000, 10)], 'max_depth':[int(x) for x in np.linspace(1, 15, 1)], 'max_features':['auto', 'sqrt'], 'bootstrap':[True, False]}

# optimize the hyperparameters via GridSearch
rf_random = RandomizedSearchCV(estimator=rf, param_distributions=random_grid, n_iter=100, cv=3, verbose=2, random_state=42, n_jobs=-1)
rf_random.fit(X_train, y_train)

# retrieve the best estimator, after hyperparameter optimization
best_model = rf_random.best_estimator_
scores_bm = cross_val_score(best_model, iris.data, iris.target, cv=10, error_score='accuracy')
print(scores.mean())  # gives us roughly 95 %
"""
old, unused code
# Set up possible values of parameters to optimize over
p_grid = {}

# Choose cross-validation techniques for the inner and outer loops,
inner_cv = KFold ...
outer_cv = KFold ...

# GridSearch cross-validation object hyperparameter optimization
clf = GridSearchCV(estimator=model, param_grid=p_grid, cv=inner_cv)

# Nested CV with parameter optimization
nested_score = cross_val_score(clf, X=X_iris, y=y_iris, cv=outer_cv)
nested_score.mean()
"""

