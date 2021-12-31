# GRADED FUNCTION:image2vector

import numpy as np


def image2vector(image):
    """
    Argument:
    image -- a numpy array of shape (length, height, depth)

    Returns:
    v -- a vector of shape (length*height*depth, 1)
    """

    # (≈ 1 line of code)
    # v =
    # YOUR CODE STARTS HERE
    v = image.reshape((image.shape[0]*image.shape[1]*image.shape[2], 1))

    # YOUR CODE ENDS HERE

    return v


# This is a 3 by 3 by 2 array, typically images will be (num_px_x, num_px_y,3) where 3 represents the RGB values
t_image = np.array([[[0.67826139,  0.29380381],
                     [0.90714982,  0.52835647],
                     [0.4215251,  0.45017551]],

                    [[0.92814219,  0.96677647],
                     [0.85304703,  0.52351845],
                     [0.19981397,  0.27417313]],

                    [[0.60659855,  0.00533165],
                     [0.10820313,  0.49978937],
                     [0.34144279,  0.94630077]]])

print("image2vector(image) = " + str(image2vector(t_image)))
