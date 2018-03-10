'''
Created on Mar 5, 2018

@author: lfko
'''


def twice(f):
    return lambda x: f(f(x))


def addThree(x):
    return x + 3


g = twice(addThree)
g(7)

print(g)
