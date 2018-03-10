'''
Created on 30.09.2017

An introduction to machine learning with scikit-learn

@author: lfko

'''
# support vector machine as classifier
from sklearn import svm

from sklearn import metrics

from sklearn import model_selection

# load the data sets we want to process on
from sklearn import datasets
from unicodedata import digit
'''
    =================   ==============
    Classes                          3
    Samples per class               50
    Samples total                  150
    Dimensionality                   4
    Features            real, positive
    =================   ==============
'''
iris = datasets.load_iris()
'''
    =================   ==============
    Classes                         10
    Samples per class             ~180
    Samples total                 1797
    Dimensionality                  64
    Features             integers 0-16
    =================   ==============
    every pixel of the image is a feature, so we have 8x8 = 64 features per sample
'''
digits = datasets.load_digits()

# data sets are typically dictionaries, with a member data (a n_features x n_samples array)
# in case we are dealing with a supervised problem the data set ought to have a target member, on which we should train and test the model
# this prints out the first digit (a 8x8 array)
print(digits.data[0])
# the digits targets are an vector of numbers from 0 to 9 (surprisingly, it is)
print(digits.target)

# get a hold of our classifier: a SVM
# gamma?
# C => our threshold regarding margin and false classification; the bigger C the more resistant is the SVM against false classifications
clf = svm.SVC(gamma=0.001, C=100.)

# before using the classifier split up the samples into training and test sets
X_train, X_test, y_train, y_test = model_selection.train_test_split(digits.data, digits.target, test_size=0.20, random_state=7)

print("data splitted up")
print(len(X_train))
print(len(X_test))
print(len(y_train))
print(len(y_test))

# now fit the model
clf.fit(X_train, y_train)
# actual prediction
prediction = clf.predict(X_test)

# now cross validate the predicted values with our test values

print("Classification report for classifier %s:\n%s\n"
      % (clf, metrics.classification_report(y_test, prediction)))
print("Confusion matrix:\n%s" % metrics.confusion_matrix(y_test, prediction))

