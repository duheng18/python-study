import numpy as np


def npSum():
    a = np.array([0, 1, 2, 3, 4])
    b = np.array([9, 8, 7, 6, 5])
    c = a ** 2 + b ** 3
    print(c)
    return c

m = np.arange(15).reshape(3, 5)
print(npSum())
print(m)
