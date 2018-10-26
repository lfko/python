'''
Created on Oct 26, 2018

@author: lfko
'''

from lfko.python.redis.db import connHandle;
from lfko.python.redis.db import redis_kv, redis_list, redis_set, redis_hash;


def main():
    rCon = connHandle.openConn('192.168.2.103');
    
    # we can just start interacting with the database
    # doKeyValueStuff(rCon);
    # doListStuff(rCon);
    # doSetStuff(rCon);
    doHashStuff(rCon);


def initDb():
    pass;


def doHashStuff(rcon):
    """ """
    hashKey = 'planes';
    parts = {'USA':'F-16', 'BRD':'Tornado', 'DDR':'MiG-21', 'UdSSR':'TU-95', 'France':'Mirage'};
    
    for key, value in parts.items():
        redis_hash.createHash(rcon, hashKey, key, value);

    redis_hash.readHash(rcon, hashKey);
    redis_hash.updateHash(rcon, hashKey, 'BRD', 'Starfighter');
    redis_hash.getValues(rcon, hashKey);
    
    redis_hash.removeKey(rcon, hashKey, 'France');
    redis_hash.getValues(rcon, hashKey);
    redis_hash.getKeys(rcon, hashKey);

    
def doSetStuff(rcon):
    setKey = 'prices';
    
    redis_set.createSet(rcon, setKey, 14.99, 7.99, 5.99, 4.50, 4.50, 3.99, 19.99);
    redis_set.readSet(rcon, setKey);
    
    # remove a specific element and re-read the set
    redis_set.removeSetElem(rcon, setKey, 14.99);
    redis_set.readSet(rcon, setKey);


def doListStuff(rcon):
    listKey = 'buildings';
    
    # buildings = ['Beuth', 'Grashof', 'Gauß', 'Bauwesen', 'Praesidium'];
    
    redis_list.createList(rcon, listKey, 'Beuth', 'Grashof', 'Gauß', 'Bauwesen', 'Praesidium');
    redis_list.readList(rcon, listKey);
    
    # okay, now we create another list
    redis_list.createList(rcon, 'studies', 'mathematics', 'computer science', 'data science', 'architecture');    
    
    # we would like to change the value at index 3 (architecture) to a new value
    redis_list.updateList(rcon, 'studies', 3, 'economics');
    redis_list.readList(rcon, 'studies');
    
    redis_list.deleteList(rcon, 'studies');


def doKeyValueStuff(rcon):
    redis_kv.createDoc(rcon, 'machine', 'intel pentium');
    resp = redis_kv.readDoc(rcon, 'machine');
    
    print('response from the database ' + str(resp));
    
    redis_kv.updateDoc(rcon, 'machine', 'AMD');

    resp = redis_kv.readDoc(rcon, 'machine');
    
    print('response from the database ' + str(resp));
    
    redis_kv.delDoc(rcon, 'machine');


if __name__ == '__main__':
    main();
