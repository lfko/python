'''
Created on Nov 1, 2018

@author: lefko
'''


def calcDist(str_one, str_two):
    """ classical levenshtein distance calculator, using nested lists """

    if str_one == str_two:
        print('Levenshtein distance is 0, because both strings are equal!')
        return 0

    # first step: determine length of strings
    n_rows = len(str_one)  # word used for constructing the lew_matr
    n_cols = len(str_two)  # word used for constructing the columns

    print(n_rows, n_cols)

    # second step: create a n x m matrix - or a multi dimensional list
    lew_matr = []
    # first column is a vector of length n_lew_matr, containg numbers from 0
    # to length of word str_one
    firstCol = list(range(0, n_rows + 1))
    lew_matr.append(firstCol)

    # loop creates the columns
    for i in range(1, n_cols + 1):
        column = []

        # append current column number as the number at the first index
        column.append(i)
        for _ in range(1, n_rows + 1):
            # fill the rest of the column with 0 for now
            column.append(0)

        # add the column
        lew_matr.append(column)

    print(lew_matr)

    # now compare the words, char by char
    # comparison is done column by row element
    for idx, s in enumerate(str_two, 1):
        # print(idx, s);
        for idy, t in enumerate(str_one, 1):
            # print(idy, t);
            # easiest result: both characters are equal
            if s == t:
                lew_matr[idx][idy] = min(
                    lew_matr[idx][idy - 1], lew_matr[idx - 1][idy], lew_matr[idx - 1][idy - 1]) + 0
            else:
                # characters are not equal, so we have to assign a new value to the cell being opened
                # the value is 1 + the minimum of either the cell on top, the
                # cell to the left OR the left diagonal cell
                lew_matr[idx][idy] = min(
                    lew_matr[idx][idy - 1], lew_matr[idx - 1][idy], lew_matr[idx - 1][idy - 1]) + 1

        # print('column ' + str(idx) + ' checked - moving on to the next one');
        # print('lewenshtein matrix so far:')
        # print(lew_matr);

    print('final lewenshtein distance matrix: ')
    print(lew_matr)

    print("Levenshtein distance for " + str_one + " and " +
          str_two + " is ", lew_matr[n_cols][n_rows])
    return lew_matr[n_cols][n_rows]


if __name__ == '__main__':
    print(calcDist("apple", "pear"))
    print(calcDist("pear", "apple"))
    print(calcDist("gambol", "gumbo"))
    print(calcDist("eagle", "raven"))
    print(calcDist("cat", "dog"))
    print(calcDist("beach", "beach"))
