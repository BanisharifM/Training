# GRADED FUNCTION: normalize_rows

import numpy as np


def normalize_rows(x):
    """
    Implement a function that normalizes each row of the matrix x (to have unit length).

    Argument:
    x -- A numpy matrix of shape (n, m)

    Returns:
    x -- The normalized (by row) numpy matrix. You are allowed to modify x.
    """

    # (≈ 2 lines of code)
    # Compute x_norm as the norm 2 of x. Use np.linalg.norm(..., ord = 2, axis = ..., keepdims = True)
    # x_norm =
    # Divide x by its norm.
    # x =
    # YOUR CODE STARTS HERE
    x_norm = np.linalg.norm(x, ord=2, axis=1, keepdims=True)
    x = x/x_norm

    # YOUR CODE ENDS HERE

    return x


x = np.array([[0, 3, 4],
              [1, 6, 4]])
print("normalizeRows(x) = " + str(normalize_rows(x)))
