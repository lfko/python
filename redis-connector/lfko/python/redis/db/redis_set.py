'''
Created on Oct 26, 2018

@author: lfko
'''


def createSet(rcon, setKey, *vals):
    """ adds an element to a (newly) created set; only new elements will be added """
    
    for val in vals:
        ret = rcon.sadd(setKey, val);
        print('element to set added? ' + str(ret));
    
    print('length of set: ' + str(rcon.scard(setKey)));

    
def readSet(rcon, setKey):
    ret = rcon.smembers(setKey);
    print(type(ret));
    print(ret);

    
def removeSetElem(rcon, setKey, elem):
    """ removes a specific element from the set """
    rcon.srem(setKey, elem);

    
def updateSetElem(rcon, setKey):
    """ there is no suitable function for that """
