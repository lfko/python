'''
Created on Oct 26, 2018

@author: lfko
'''
import redis;


def openConn(hostname='localhost'):
    """ open a connection to a redis db and returns a connection handle """
    
    # open connection to the default db on localhost
    rCon = redis.StrictRedis(host=hostname, port=6379, db=0);
    
    return rCon;
