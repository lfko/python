'''
Created on Oct 31, 2018

@author: Florian "lefko" Becker, s76343

    code for the exercise assignment_02 
'''

import random


def assignment_02_01(*args):
    """ multiplies an arbitrarily long list of number arguments and returns the result"""

    if len(args) == 0:
        print('no argument supplied')
        return 0
        # maybe raising an exception is a bit too harsh
        # raise BaseException('no arguments supplied');

    # check the type of all elements in the list; if not all of them are numbers, then raise an exception
    # this is maybe computational to exhausting, supposing we have a very
    # large list ...
    if all(isinstance(n, int) for n in args) is False:
        raise TypeError('no numbers were supplied')

    # init the result variable
    result = 1

    # iterate through the list of arguments and calculate the product
    for num in args:
        result = result * num

    # return the final result
    return result


def assignment_02_02a(numberList):
    """ For each element of the input list, the function should add a string "higher" if the element was larger than 5 and "lower" otherwise """

    if(len(numberList) == 0):
        raise TypeError('function excepts a list of number')
    if all(isinstance(n, int) for n in numberList) is False:
        raise TypeError('no numbers were supplied')

    # lambda magic: via map we apply the same function to a number of elements
    # here, we apply the if ... else ... to check, whether an element of the list is less or greater then 5
    # it then returns the string "higher" or "lower", depending on the outcome of the test
    # since map returns an iterator, we write directly into a list
    result = list(map(lambda x: "higher" if x > 5 else "lower", numberList))

    return result


def assignment_02_02b(numberList):
    """ For each element of the input list, the function should add a string “higher” if the element was larger than 5 and “lower” otherwise """

    if(len(numberList) == 0):
        raise TypeError('function excepts a list of number')
    if all(isinstance(n, int) for n in numberList) is False:
        raise TypeError('no numbers were supplied')

    # now we do the same with list-comprehension; quite self-explanatory
    result = ["higher" if num > 5 else "lower" for num in numberList]

    return result


def generate_random_student_pairs(studentsList):
    """ extra task:  randomly pair students and return the all the tuples. No student shall be paired with her or himself"""

    # empty list of pairs - pairs will be tuples
    pairs = []

    # check if there is an odd number of students in the list
    # if so, create one pair, consisting only of a randomly picked student
    if len(studentsList) % 2 == 1:
        # odd number of students in the list - there will be one residual
        # student, which cannot be paired
        randStudent = random.choice(studentsList)
        lonelyOne = (randStudent, '')
        # remove her/him
        studentsList.remove(randStudent)
        # ... and add the pair
        pairs.append(lonelyOne)

    # now iterate the list of students
    for student in studentsList:

        # remove the element from the list, to avoid doubling
        studentsList.remove(student)
        # pick a random student to pair with
        randStudent = random.choice(studentsList)

        # they do not equal, so let's pair them
        if randStudent != student:
            newPair = (student, randStudent)
            pairs.append(newPair)
            studentsList.remove(randStudent)

        print('residual student list ', studentsList)

    # TODO for some reason, there are two left if the list is long enough. I do not know right now why
    # but for now just create a pair with the remaining two students
    if len(studentsList) == 2:
        pairs.append((studentsList[0], studentsList[1]))

    return pairs


class Duck:
    """ class defining a Duck object """

    def __init__(self, *names):
        """  pythonesque constructor """

        self.name = ''
        if all(isinstance(namestr, str) for namestr in names) is False:
            print('no valid names supplied; must be type string - name will be empty')
        else:
            # iterate the names supplied and concatenate them as the name string
            # for nstr in names:
                # TODO there gotta be a better way achieve this ...
            #    self.name += nstr + ' ';
            self.name = ' '.join(names)

            # a final rstrip() to remove the right outermost space
            self.name = self.name.rstrip()

    def talks_to(self, anotherDuck):
        """ the duck shall talk to another object, preferably an instance of class Duck """
        if isinstance(anotherDuck, Duck):
            # instance of class Duck talks to instance of class Duck
            return "Quak"
        else:
            # supplied object is not an instance of class Duck
            raise ValueError("Can only talk to other Ducks")

    def __repr__(self):
        """ will be called if just the name of the variable/object is typed """
        return "Quak! My name is %s" % self.name

    def __str__(self):
        """ print a readable message (representation of the object) """
        return "Hello! All day I quak! Quak!"


""" for testing purposes only 

if __name__ == '__main__':
    
    studentsList = ['Manfred', 'Heike', 'Clara', 'Sandro', 'Sabine', 'Enrique', 'Anna', 'Katharina', 'Torsten'];
    print(generate_random_student_pairs(studentsList));
    studentsList = ['Manfred', 'Heike', 'Clara'];
    print(generate_random_student_pairs(studentsList));
    studentsList = ['Manfred', 'Heike', 'Clara', 'Sandro', 'Sabine', 'Erika'];
    print(generate_random_student_pairs(studentsList));


    assignment_02_01();
    # assignment_02_01(1, "du", "da");
    res = assignment_02_01(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
    print(res);
    res = assignment_02_02a([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
    print(res);
    res = assignment_02_02b([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
    print(res);
    
    derp = Duck(1, 2, 3);
    
    du = Duck("Alfred", "Judokus", "Quak");
    print(du.name);
    print(du.__repr__);
    du = Duck("Quak");
    print(du.name);
    print(du);
    du;
    duck2 = Duck();
    print(du.name);
    try:
        duck2.talks_to("Crocodile");
    except ValueError as ve:
        print(ve);
        assert str(ve) == 'Can only talk to other Ducks';
"""
