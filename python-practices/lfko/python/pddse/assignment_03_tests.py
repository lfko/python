import assignment_03 as a
import numpy as np

def assignment_03_01_test():
    correct = np.array([ 0,  3,  6,  9, 12, 15, 18, 21, 24, 27, 30])
    assert np.array_equal(a.assignment_03_01(), correct)

def assignment_03_02_test():
    correct = np.array([[ 1.,  2.,  3.,  4.,  5.],
                        [ 0.,  1.,  2.,  3.,  4.],
                        [-1.,  0.,  1.,  2.,  3.],
                        [-2., -1.,  0.,  1.,  2.]])
    assert np.array_equal(a.assignment_03_02(), correct)

def assignment_03_03_test():
    arr = np.array([[ 1.,  2.,  3.,  4.,  5.],
                    [ 0.,  1.,  2.,  3.,  4.],
                    [-1.,  0.,  1.,  2.,  3.],
                    [-2., -1.,  0.,  1.,  2.]])
    correct = np.array([[1., 2., 3.],
                        [0., 1., 2.]])
    assert np.array_equal(a.assignment_03_03(arr), correct)

def assignment_03_04_test():
    result = a.assignment_03_04()
    true_mean = np.array([1,-2])
    true_std = np.array([2., 0.5])
    mean_diff = result.mean(axis=0) - true_mean
    std_diff = result.std(axis=0) - true_std
    assert all(np.hstack([mean_diff, std_diff]) < 0.1)


if __name__ == '__main__':
    assignment_03_01_test()
    assignment_03_02_test()
    assignment_03_03_test()
    assignment_03_04_test()
