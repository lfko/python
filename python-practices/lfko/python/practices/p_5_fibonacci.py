'''
Created on Oct 17, 2018

@author: lfko
    
    computes the fibonacci sequence
'''


def main():
    
    count = getIntInput();
    
    # initial starting variables
    n_1 = 1;
    n_2 = 0;
    
    fiboList = [];
    
    # start iterating
    for n in range(1, count):
        print('current iteration ', n);
        fiboNum = generateFiboNum(n, n_1, n_2);
        print('calculated Fibonacci number: ', fiboNum);
        
        n_2 = n_1;
        n_1 = fiboNum;
        
        fiboList.append(fiboNum);
        print('\n');
    
    print('calculation for ', count, ' numbers finished \n');
    print('showing all Fibonacci numbers: ', fiboList);


def getIntInput(cli_text="How many Fibonacci numbers should be generated?"):
    """ asks for user input - cli_text is a default text parameter, but could be overwritten """
    return int(input(cli_text));


def generateFiboNum(n, n_1_iter, n_2_iter):
    """ 3 parameters: n -> current iteration
                      n_1_iter -> previous iteration
                      n_2_iter -> iteration before the previous iteration """
    
    newFiboNum = n_1_iter + n_2_iter;
    # print('next Fibonacci number ', newFiboNum);
    
    return newFiboNum;


if __name__ == '__main__':
    main();
