# GRADED FUNCTION: L1

import numpy as np


def L1(yhat, y):
    """
    Arguments:
    yhat -- vector of size m (predicted labels)
    y -- vector of size m (true labels)

    Returns:
    loss -- the value of the L1 loss function defined above
    """

    # (≈ 1 line of code)
    # loss =
    # YOUR CODE STARTS HERE
    loss = np.sum(np.abs(y-yhat))

    # YOUR CODE ENDS HERE

    return loss


yhat = np.array([.9, 0.2, 0.1, .4, .9])
y = np.array([1, 0, 0, 1, 1])
print("L1 = " + str(L1(yhat, y)))
