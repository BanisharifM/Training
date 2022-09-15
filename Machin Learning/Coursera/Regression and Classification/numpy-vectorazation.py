import numpy as np
import time

a=np.zeros(4)
print(f"np.zeros(4): a= {a}, a shape= {a.shape}, a data type = {a.dtype}")

a=np.zeros((4,))
print(f"np.zeros(4): a= {a}, a shape= {a.shape}, a data type = {a.dtype}")

a=np.random.random_sample(4)
print(f"np.zeros(4): a= {a}, a shape= {a.shape}, a data type = {a.dtype}")

a=np.arange(4.)
print(f"np.zeros(4): a= {a}, a shape= {a.shape}, a data type = {a.dtype}")

a=np.arange(10)
print(a[:3])
print(a[3:])
print(a[2:7:2])




