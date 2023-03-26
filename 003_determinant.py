'''The determinant is computed via LU factorization using the LAPACK routine z/dgetrf.'''

import numpy as np
a = np.array([[1,2],[3,4]])
c = np.linalg.det(a)
print(c)


a = np.array([ [[1, 2], [3, 4]], [[1, 2], [2, 1]], [[1, 3], [3, 1]] ])

print(a.shape)
print(np.linalg.det(a))
