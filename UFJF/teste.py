import numpy as np

dist_TORRES = np.array([0, 475, 900, 1500, 1860, 2300, 2500])

for i in range(np.shape(dist_TORRES)[0]-1):
    print(dist_TORRES[i], dist_TORRES[i+1])
