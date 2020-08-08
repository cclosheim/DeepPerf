import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt
from random import shuffle, gauss

randomlist = []
for i in range(1000000):
    randomNums = int(gauss(5,3))
    randomlist.append(randomNums)

randomNums = np.random.normal(loc=5, scale=3, size=1000000)
print(randomlist)
plt.hist(randomNums)
plt.hist(randomlist)
plt.show()