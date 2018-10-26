'''
Created on Oct 26, 2018

@author: lfko
'''


def createHash(rcon, hashKey, key, value):
    """ add a new key value pair into the hash """
    rcon.hset(hashKey, key, value);


def readHash(rcon, hashKey):
    """ retrieve the value for a specific key - or all elements, if *keys is empty """
    ret = rcon.hgetall(hashKey)

    print('retrieved the hash values ' + str(ret));

    
def updateHash(rcon, hashKey, key, value):
    """ update the value for a given key in the hash """
    rcon.hset(hashKey, key, value);


def removeKey(rcon, hashKey, key):
    """ """
    ret = rcon.hdel(hashKey, key);
    
    print('field removed? ' + str(ret));

    
def getKeys(rcon, hashKey):
    """ retrieve all keys of the hash """
    ret = rcon.hvals(hashKey);
    
    print('values in hash: ' + str(ret));

    
def getValues(rcon, hashKey):
    """ retrieve all values of the hash """
    ret = rcon.hkeys(hashKey);
    
    print('keys in hash: ' + str(ret));
