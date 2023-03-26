'''
shape and size of an array
'''

import numpy as np

array_eg = np.array([[[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[0 ,1 ,2, 3],
                           [4, 5, 6, 7]]])

print(array_eg.ndim)
print(array_eg.size)
print(array_eg.shape)



