'''
Created on 26.10.2017

@author: lfko
'''
from builtins import str

# print out some simple list contens


def lefko():
    print('kill or be killed')


def simpleAddition(a, b):
    print("a: ", a)
    print("b: ", b)
    c = a + b
    print(c)  


def main():

    Items = "Sword", "Helmet", "Armor", "Mace", "Ring", "Boots"
    
    # iterate the list/array?
    for item in Items:
        print(item)
        
    # can do this
    print('hello there')
    
    # or this
    print("I'm baroque obama.")
    print('thank you for your time')
    
    # but cannot do this
    # print("My cock is actually " + 9 + " inches longer than yours")
    
    # how about convert it to a string
    print(str(9) + " inches")
    
    # escape quotes
    print('We\'re going to the market to say "Hi"')
    
    # some math
    print(1 + 2)
    print(2 - 3)
    print(3 / 4)
    print(4 * 4)
    # exponential 
    print(4 ** 4)
    
    # print = print(10)
    # print = None
    # fails
    # print(print)
    
    simpleAddition(10, 10)
    simpleAddition(b=12, a=13)
    
    myVar = 5
    if myVar is None:
        print('it is None')
    else:
        lefko()
      
    
if __name__ == "__main__":
    main()  

