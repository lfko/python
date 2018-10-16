'''
Created on Oct 14, 2018

@author: lfko

    a program, that - for a given number - finds all the eglible divisors (the ones, where the remainder is 0)
'''
import itertools


def findDivisors(number):
    """ find all divisors for the given number """  
    for x in itertools.count():
            if(x == 0):
                continue;
            if (number % x == 0):
                print('{:.0f}'.format(x), ' is a divisor of ', number);
                print('result {:.0f}'.format(number / x))
            
            if(x > number):
                print('-----------------------')
                break;


if __name__ == '__main__':
    findDivisors(10);
    findDivisors(20);
    findDivisors(300);
    findDivisors(1898);
    findDivisors(473);
