'''
Created on 20.09.2017

@author: lfko
'''


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



# one dot for the relative path
data_train = pd.read_csv('./input/train.csv')
sample_data = data_train.sample(3)

# plots a barplot showing the correlation between the given parameters
# output is already showing the estimates, or the tendency for a certain variable  
sns.barplot(x="Pclass", y="Survived", hue="Sex", data=data_train);
# with this plot we see, that there is clearly a correlation between price class and chance of survival
plt.show()

# this does not really work because every(!) age would be used as a x value, which in the end will cause a definite ovefitting
sns.barplot(x="Age", y="Survived", hue="Sex", data=data_train);
# so we do not use this plot right now because we have to group the ages into logical groups
# plt.show()
