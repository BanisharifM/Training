import numpy as np
import math
from public_tests import *

# GRADED FUNCTION: basic_sigmoid


def basic_sigmoid(x):
    """
    Compute sigmoid of x.

    Arguments:
    x -- A scalar

    Return:
    s -- sigmoid(x)
    """
    # (≈ 1 line of code)
    # s =
    # YOUR CODE STARTS HERE
    s = 1 / (1 + math.exp(-x))
    # YOUR CODE ENDS HERE

    return s


print("basic_sigmoid(1) = " + str(basic_sigmoid(1)))

# basic_sigmoid_test(basic_sigmoid)


# example of np.exp
t_x = np.array([1, 2, 3])
print(np.exp(t_x))  # result is (exp(1), exp(2), exp(3))
# example of vector operation
t_x = np.array([1, 2, 3])
print(t_x + 3)
