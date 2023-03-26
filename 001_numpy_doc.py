from ast import Num
from turtle import shape
import numpy as np

a = np.arange(6)
a2 = a[np.newaxis , : ]
print(a2.shape)
print(a)
print(a2)
print(a[0])
a3 = np.array([[1,2,3,4],[3,4,5,6,7]])
print(a3)
print(a3[0])

'''nd array 
~ The NumPy ndarray class is used to represent both matrices and vectors. A vector is an array with a single dimension 

 while a matrix refers to an array with two dimensions. For 3-D or higher dimensional arrays, the term tensor is also commonly used.
 In NumPy, dimensions are called axes.

'''


"""create a array """

# arry1 = np.zeros(10)
# array2 = np.ones(10)
# array3 = np.empty(20)
# print(type(array3))
# print(array3.shape)
# print(f"{arry1} \n\n {array2}\n\n{array3}")
# print(np.arange(10))
# ar5 = np.arange(10,50,5)    # 5 is the difference between array 
# print(ar5)

arr6 = np.linspace(0 , 10 , num= 2000)   # np.linspace() to create an array with values that are spaced linearly in a specified interval: 
print(arr6)

'''
specifing a data type to an array element 
'''

x = np.ones(10 , dtype=np.float32)
print(x)







