'''Matrix or vector norm.

This function is able to return one of eight different matrix norms, or one of an infinite number of vector norms (described below), depending on the value of the ord parameter.'''
import numpy as np
from numpy import linalg as LA

a = np.arange(9) -4  # the array will start from (-4)
print(a)

b = a.reshape((3,3))
print(b)

print(LA.norm(a))
print(LA.norm(b))
print(LA.norm(b,'fro'))
print(LA.norm(a,np.inf))
print(LA.norm(a,-np.inf))
print(LA.norm(b,-np.inf))




