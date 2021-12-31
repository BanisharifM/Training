# GRADED FUNCTION: softmax

import numpy as np


def softmax(x):
    """Calculates the softmax for each row of the input x.

    Your code should work for a row vector and also for matrices of shape (m,n).

    Argument:
    x -- A numpy matrix of shape (m,n)

    Returns:
    s -- A numpy matrix equal to the softmax of x, of shape (m,n)
    """

    # (≈ 3 lines of code)
    # Apply exp() element-wise to x. Use np.exp(...).
    # x_exp = ...

    # Create a vector x_sum that sums each row of x_exp. Use np.sum(..., axis = 1, keepdims = True).
    # x_sum = ...

    # Compute softmax(x) by dividing x_exp by x_sum. It should automatically use numpy broadcasting.
    # s = ...

    # YOUR CODE STARTS HERE
    x_exp = np.exp(x)
    x_sum = np.sum(x_exp, axis=1, keepdims=True)
    s = x_exp/x_sum

    # YOUR CODE ENDS HERE

    return s


t_x = np.array([[9, 2, 5, 0, 0],
                [7, 5, 0, 0, 0]])
print("softmax(x) = " + str(softmax(t_x)))
