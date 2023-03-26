import numpy as np 

'''
memory layout and attribute of nd array 
'''

arr = np.array([[10,20,30],[20,30,40],[30,40,50]])
# print(arr.flags(True))
print(arr.shape)
print(arr.flags)   # information about memory 
print(arr.strides)  #Tuple of bytes to step in each dimension when traversing an array
print(arr.ndim)  # dimention 

print(arr.itemsize)   # length of array element in  byte 
print()
print(arr.nbytes)   # total byte consumed by an array   
print(arr.base)    # Base object if memory is from some other object.
print(arr.data)   # base address 