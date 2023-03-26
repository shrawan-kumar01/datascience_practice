'''
UNIQUE AND OTHER SET OPERATION
np.unique() -------- > return :~ sorted unique value in arryay
'''
from re import X
from tkinter import Y
import numpy as np 

arr = np.array([1,2,1,2,3,1,555,5,5,5,5,])
# arr.unique()
# print(arr)     #AttributeError: 'numpy.ndarray' object has no attribute 'unique'

arr_uni = np.unique(arr)
print(arr_uni)


'''
np.in1d() --------->test membership of array in another aarry 
'''
arr = np.array([1,2,1,2,3,1,555,5,5,5,5,])
# print(arr.in1d([1,555,5]))    # AttributeError: 'numpy.ndarray' object has no attribute 'in1d'

arr_find = np.in1d(arr,[1,555])         #[ True False  True False False  True  True False False False False]
print(arr_find)


#  intersect1d(x,y)    compute the intersectyion of the array 
X = np.array([1,2,3,4,5,5,6,10])
Y = np.array([1,2,100,20,5])

arr_intersect = np.intersect1d(X,Y)
print(arr_intersect)

#  union1d()  ---- print the union of twio array 
arr_union = np.union1d(X,Y)
print(arr_union)
#  setdiff1d(x,y)  -----> check the set difference ,,,, element present in x not in y 

arr_setdiff  = np.setdiff1d(X,Y)
print(arr_setdiff)
#  setxorid(x,y) ---- compute the symmetric difference , elementr thet are in ether of te element but not in both 

arr_xorid = np.setxor1d(X,Y)
print(arr_xorid)



