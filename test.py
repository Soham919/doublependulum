import numpy as np

a = np.array([2,1,3,11,4,5,7,6,23,56,114,2,4,89])
a_ind = a.flatten().argsort()[::-1]
a_sort = a.argsort()[::-1]
print(a_sort)
print(a_ind)
