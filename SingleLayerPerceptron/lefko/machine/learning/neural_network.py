'''
Created on 21.09.2017

@author: lfko
'''

# also goes by the name scikit-learn
import sklearn
import sklearn.datasets as skd
import sklearn.linear_model
import matplotlib.pyplot as plt
import numpy as np

    
print("main called - ending")
    
    
# Generate a dataset and plot it
np.random.seed(0)
# this generate two intertwine 'moon'-shaped data aggregations
X, y = skd.make_moons(200, noise=0.20)
plt.scatter(X[:, 0], X[:, 1], s=40, c=y)

# show the plotted diagram
plt.show()

# Train the logistic rgeression classifier
clf = sklearn.linear_model.LogisticRegressionCV()
clf.fit(X, y)
 
# Plot the decision boundary
# plot_decision_boundary(lambda x: clf.predict(x))
plt.title("Logistic Regression")


# Helper function to plot a decision boundary. 
# If you don't fully understand this function don't worry, it just generates the contour plot below. 
def plot_decision_boundary(pred_func): 
    # Set min and max values and give it some padding 
    x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5 
    y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5 
    h = 0.01 
    # Generate a grid of points with distance h between them 
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h)) 
    # Predict the function value for the whole gid 
    Z = pred_func(np.c_[xx.ravel(), yy.ravel()]) 
    Z = Z.reshape(xx.shape) 
    # Plot the contour and training examples 
    plt.contourf(xx, yy, Z) 
    plt.scatter(X[:, 0], X[:, 1], c=y) 
    
print()    
# prevents the script from being called, if it is solely imported as a module
# if __name__ == "__main__":
#    main()
