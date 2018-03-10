'''
Created on 18.10.2017

@author: lfko
'''

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
from sklearn import svm

# our x and y coordinates
x = [1, 5, 1.5, 8, 1, 9]
y = [2, 8, 1.8, 8, 0.6, 11]

# translate them into a numpy feature vector, with x and y as its features
X = np.array([[1, 2],
             [5, 8],
             [1.5, 1.8],
             [8, 8],
             [1, 0.6],
             [9, 11]])

# labels, which means these are the target values for our vectors - or differently expressed as classes
# coincidentily vectors with low numbers are assigned 0, while high valued vectors are assigned 1
Y = [0, 1, 0, 1, 0, 1]

clf = svm.SVC(kernel='linear', C=1.0)

# visualize the feature vectors
# plt.scatter(x, y)
# plt.show()

# train the classifier
clf.fit(X, Y)

# create a 2D numpy test array
X_test = np.array([[0.58, 0.76], [10.52, 9.83]])

# predict the class (should be 0)
print(clf.predict(X_test))

w = clf.coef_[0]
print(w)

a = -w[0] / w[1]

xx = np.linspace(0, 12)
yy = a * xx - clf.intercept_[0] / w[1]

h0 = plt.plot(xx, yy, 'k-', label="non weighted div")

plt.scatter(X[:, 0], X[:, 1], c=y)
plt.legend()
plt.show()
