'''
Created on Oct 14, 2018

@author: lfko

    find overlapping elements in two data sets (e.g. lists)

'''

import random;

list_a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
list_c = ['germany', 'estonia', 'norway', 'turkey']; 
list_d = ['england', 'estonia', 'sweden', 'turkey', 'morroco', 'hungary'];


def findOverlap(setA, setB):
    """ compare two data sets A and B and find overlapping elements and print them """
    
    res = __elem_wise_cmp__(setA, setB);
    print(' the normal way ', res, type(res));

    # or use filter instead. It creates a list of elements for which a function returns true.
    # TODO map with multiple list actions
    # res = map(lambda x, y: __elem_wise_cmp(x, y), setA, setB);
    # print(res, type(res));

    # list comprehension
    res = [elemA for elemA in setA for elemB in setB if elemA == elemB];
    print(' using list comprehension ', res, type(res));


def __elem_wise_cmp__(setA, setB):
    overlaps = [];
    for elemA in setA:
        if elemA in setB:
            overlaps.append(elemA);

    return overlaps;


def gen_random_list():
    l = [];
    for i in range(15):
        # aqcuire a random integer between 1 and 1000
        l.append(random.randint(1, 50));

    print(' new list, containing random numbers: ', l);
    return l;


if __name__ == '__main__':
    findOverlap(list_a, list_b);
    findOverlap(list_c, list_d);
    findOverlap(gen_random_list(), gen_random_list());
