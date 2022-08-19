import numpy as np
import math

print(math.sin(2))

print(math.cos(2))

print(np.array([1, 2.1, 3, 4], dtype='int'))

print(np.array([range(i, i+3) for i in [2, 4, 6]]))

print(np.zeros(10, dtype='int'))

print(np.ones((3, 5), dtype='int'))

print(np.full((3,5), 3.14))

print(np.arange(2,21,2))

print(np.linspace(0,1,5))

print(np.random.random((3,5)))

print(np.random.randint(0,10,(3,5)))