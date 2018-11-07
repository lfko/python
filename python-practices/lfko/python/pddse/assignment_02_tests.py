import assignment as a;


def assignment_02_01_test():
    assert a.assignment_02_01(1, 2, 3) == 6


def assignment_02_02a_test():
    numbers = [1, 6]
    assert a.assignment_02_02a(numbers) == ['lower', 'higher']


def assignment_02_02b_test():
    numbers = [1, 6]
    assert a.assignment_02_02b(numbers) == ['lower', 'higher']


def assignment_02_03_test():
    duck = a.Duck("Alfred", "Judokus", "Quak")
    assert duck.name == 'Alfred Judokus Quak'

    other_duck = a.Duck("Hans", "Peter", "Schnabel")
    assert other_duck.name == 'Hans Peter Schnabel'
    assert duck.talks_to(other_duck) == "Quak"

    try:
        duck.talks_to("Crocodile")
    except ValueError as ve:
        assert str(ve) == "Can only talk to other Ducks"


if __name__ == '__main__':
    assignment_02_01_test()
    assignment_02_02a_test()
    assignment_02_02b_test()
    assignment_02_03_test()
