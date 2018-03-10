'''
Created on 24.09.2017

@author: lfko
'''


import sklearn
import numpy
import pandas
import matplotlib.pyplot as plt

def main():
    # #
    print("-- main called --")
    
    print("reading sample set")
    names = ["PassengerId", "Survived", "    Pclass", "Name", "Sex", "Age", "SibSp", "Parch", "Ticket", "Fare", "Cabin", "Embarked"]
    data_train = pandas.read_csv('./input/train.csv', names=names)
    print(data_train.shape)
    
    data_train.set_index("PassengerId", inplace=True)
    print(len(data_train))
    
    plt.plot(data_train)
    plt.show()
    # #
    

if __name__ == '__main__':
    main()
