'''
OPERATION ON NUM PY ARRAY 

'''
from cgi import print_form
import numpy as np 

#  any arithmetic operation on equal-size array apply element wiase 

arr = np.array([[1.,2.,3.,],[4.,5.,6.,]])
# print(arr)
# print(arr * arr *arr)   # multiply each element thrice
# print(arr - arr)
# print(arr + arr)
# print(arr /arr)
# print(arr % 2)     
# print(arr *10)       #propagating to each element 

'''
operation between different size of array is called  BROADCASTING  will be discussed later in this chapter
'''



print(arr[0:2])
arr_slice = np.array([1,2,3,4,5,6])
print(arr_slice[0:1])
print(arr_slice[0:])
print(arr_slice[:])
#  broadcasting value to entire section of the array 

arr_slice[1:4] = 100
print(arr_slice)
#  array slice are view to original data , array is not copied , whatever changes is made will reflect to original source array 

arr_slice[:] = 64
print(arr_slice)
arr_slice[1:4].copy()    # it will not create a view , insteed it will copy a original array 
print(arr_slice)

arr_slice_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(arr_slice_2d)
# arr_sliced= arr_slice_2d[0][2]
arr_sliced= arr_slice_2d[0,2]
print(arr_slice_2d.shape)
print(arr_slice_2d.ndim)
print(arr_sliced)

arr_multid = np.array([[[1,2,3],[4,5,6],[7,8,9],[10,20,30],[40,50,60]]])
print(arr_multid)
print(arr_multid.shape)
print(arr_multid.ndim)

print(arr_multid[0].shape)
print(arr_multid[0])
# print(arr_multid[1,3])          #IndexError: index 1 is out of bounds for axis 0 with size 1
print(arr_multid[0,2])          #  [7 8 9]

#    both scaler value and array can be copied to arr_multid[0]

old_array = arr_multid[0].copy()
arr_multid[0] = 42
print(arr_multid)
arr_multid[0] = old_array
print(arr_multid)

print(arr_multid[0,1])  #[4 5 6]   # it gives all the value having starting indices (0,1) in an 1D array 
# print(arr_multid[1,0])              #IndexError: index 1 is out of bounds for axis 0 with size 1










