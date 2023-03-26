'''
transposing an array:

it create a view 
jsut a special case of slicing 
numpy has special Tattribute
'''
import numpy as np 

arr = np.arange(15).reshape(3,5)
print(arr)

print("it is the t method of array transpose")

arr_transpose = arr.T
print(arr_transpose)

"""
use of transposer :~ 
inner matrices prodict [X^T.X] USING np.dot
"""
arr_i = np.random.randn(6,3)
arr_inner_pdt = np.dot(arr_i.T,arr_i)
print(arr_inner_pdt)















