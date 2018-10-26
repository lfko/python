'''
Created on Oct 26, 2018

@author: lfko
'''


def createList(rcon, listKey, *elems):
    """ creates a list of elements of arbitrary length """
    
    lst = [];
    for arg in elems:
        lst.append(arg);
    print(lst);
    
    ret = '';
    for elem in elems:
    
        # push elements onto the list with the specified key
        ret = rcon.lpush(listKey, elem);
        # *elems is just a single value
    
    print('list of length ' + str(ret) + ' created');

    
def updateList(rcon, listKey, index, value):
    """ update a value from the list to the supplied value """
    ret = rcon.lset(listKey, index, value);

    print('list updated - ' + str(ret));


def deleteList(rcon, listKey):
    """ there is no command to delete all list entries at once - we need to pop them from the list one by one """
    
    while rcon.llen(listKey) > 0:
        rcon.lpop(listKey);
        
    if rcon.llen(listKey) == 0:
        print('all elements deleted');


def readList(rcon, listKey):
    """ since there is no plain read mechanism for lists, we use lpop to retrieve (and delete) an element from the list """
    vals = [];
    
    while rcon.llen(listKey) > 0:
        vals.append(rcon.lpop(listKey));

    for val in vals:
        print('list value ' + str(val));
