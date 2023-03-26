# datascience_practice
dot product of two matrices

'''
dot product of tw o matrices

'''
'''
If both a and b are 1-D arrays, it is inner product of vectors (without complex conjugation).

If both a and b are 2-D arrays, it is matrix multiplication, but using matmul or a @ b is preferred.

If either a or b is 0-D (scalar), it is equivalent to multiply and using numpy.multiply(a, b) or a * b is preferred.

If a is an N-D array and b is a 1-D array, it is a sum product over the last axis of a and b.

If a is an N-D array and b is an M-D array (where M>=2), it is a sum product over the last axis of a and the second-to-last axis of b:
'''

# dot(a, b)[i,j,k,m] = sum(a[i,j,:] * b[k,:,m])
import numpy as np 
my_arr1 = np.array([3,4])
print(type(my_arr1))
my_arr2 = np.array([4,3])
print(np.dot(my_arr1,my_arr2))

# it take two argument as array   np.dot(my_arr1,my_arr2)a

# my_comp = np.array([2j,3j],[2j,3j])
# print(my_comp.ndim())

# my_comp2 = np.array([])
# print(np.dot(my_comp))



'''for to d array its matrix product '''

a = np.array([[1,0],[0,1]])
b =np.array([[4,1],[2,2]])
print(type(a))
c = np.dot(a,b)
print(c)


'''linalg.multi_dot(arrays, *, out=None)[source]'''

# If the first argument is 1-D it is treated as a row vector. If the last argument is 1-D it is treated as a column vector. The other arguments must be 2-D.



************************************************









