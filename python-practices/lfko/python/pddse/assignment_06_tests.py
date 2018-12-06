import os

from lfko.python.pddse import assignment_06 as a

beuth_url = "https://de.wikipedia.org/wiki/Beuth_Hochschule_f%C3%BCr_Technik_Berlin"


def assignment_06_01_test():
    assert a.assignment_06_01() == 203455


def assignment_06_02_test(url):
    infobox = a.assignment_06_02(beuth_url)
    assert infobox['Ort'] == 'Berlin-Wedding'


def assignment_06_03_test():
    assert a.assignment_06_03() == 'Steglitz-Zehlendorf'


if __name__ == '__main__':
    assignment_06_01_test()
    assignment_06_02_test(beuth_url)
    assignment_06_03_test()
