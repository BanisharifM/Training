# GRADED FUNCTION: sigmoid

import numpy as np


def sigmoid(x):
    """
    Compute the sigmoid of x

    Arguments:
    x -- A scalar or numpy array of any size

    Return:
    s -- sigmoid(x)
    """

    # (≈ 1 line of code)
    # s =
    # YOUR CODE STARTS HERE

    s = 1/(1+np.exp(-x))

    # YOUR CODE ENDS HERE

    return s


t_x = np.array([1, 2, 3])


print("sigmoid(t_x) = " + str(sigmoid(t_x)))

# sigmoid_test(sigmoid)
