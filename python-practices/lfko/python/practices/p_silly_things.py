'''
Created on Oct 15, 2018

@author: lfko
'''


def listCompress():
    """ compress a list down to certain count of elements """
    # example list
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100];

    # let us now say, that we'd like to extract only the even elements (or something similar)
    a_even = [x for x in a if x % 2 == 0];
    print(a_even);

    a_even = list(filter(lambda x: x % 2 == 0, a));
    print(a_even);


if __name__ == '__main__':
    listCompress();
