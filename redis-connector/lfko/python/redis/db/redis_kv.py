'''
Created on Oct 26, 2018

@author: lfko
'''


def createDoc(rcon, key, value):
    """ insert a new document """
    ret = rcon.set(key, value);    
    print("createDoc returns " + str(bool(ret)));


def readDoc(rcon, key):
    """ read a key and prints the corresponding value """
    # print('value for key "' + key + '" : ' + rcon.get(key) + '\n');   
    return rcon.get(key);


def updateDoc(rcon, key, value):
    """ update a key for a given document """
    ret = rcon.set(key, value);
    print("updateDoc returns " + str(bool(ret)));
    print('\n')

    
def delDoc(rcon, key):
    """ delete a document """
    ret = rcon.delete(key);
    print("delDoc returns " + str(bool(ret)));
    print('\n')
