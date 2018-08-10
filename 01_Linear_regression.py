import matplotlib.pyplot as plt
import numpy as np

from sklearn import datasets, linear_model

house_price = [240, 312, 279, 308, 199, 219, 405, 324, 319, 255]
size = [1400, 1600, 1700, 1875, 1100, 1550, 2350, 2450, 1425, 1700]

size2 = np.array(size).reshape((-1, 1))
