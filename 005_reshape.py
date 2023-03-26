from array import array
import numpy as np
a = np.arange(10)
# print(a)
# print(a.reshape(5,2))

'''With np.reshape, you can specify a few optional parameters:
'''

b = np.reshape(a,newshape = 10,order='f')
print(b)

'''order: C means to read/write the elements using C-like index order, F means to read/write the elements using Fortran-like index order, A means to read/write the elements in Fortran-like index order if a is Fortran contiguous in memory, C-like order otherwise. (This is an optional parameter and doesn’t need to be specified.)'''

'''
f ~ store array like furtron like indexing where column verys first :~~~~~~~~~~~~~~ COLUMN MAJOR LANGUAGE 
WHILE 

c ~ RAW MAJOR LANGUAGE 

'''

# How to convert a 1D array into a 2D array (how to add a new axis to an array


# You can use np.newaxis{increase the dimension by one dimension } and np.expand_dims to increase the dimensions of your existing array.

x = np.array([1,2,3,4,5,6])
print(x.shape)
x_rawaxis = x[np.newaxis,:]   # extend a dimension along a row 
print(x_rawaxis)
print(x_rawaxis.shape)
x_couaxis = x[:, np.newaxis]     # extend a dimension along column 
print(x_couaxis.shape)


'''
we can expand an array by  inserting a new axis at a specific position with {np.expand_dims}
'''

array_eg = np.array([[[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[0 ,1 ,2, 3],
                           [4, 5, 6, 7]]])

print(array_eg.shape)

array_expand0 = np.expand_dims(array_eg,axis=0)
array_expand1 = np.expand_dims(array_eg,axis=1)
array_expand2 = np.expand_dims(array_eg,axis=2)
array_expand3 = np.expand_dims(array_eg,axis=3)

print(array_expand0)
print(array_expand1)
print(array_expand2)
print(array_expand3)


print(array_expand0.shape)
print(array_expand1.shape)
print(array_expand2.shape)
print(array_expand3.shape)


























