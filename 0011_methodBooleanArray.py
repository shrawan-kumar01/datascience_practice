'''
methods for boolean array 
.sum is often used tio counting the true value of an array 
'''

from cgi import print_arguments
import numpy as np 
arr = np.random.randn(4,4)
'''print(arr>0).sum()   # it count the no of values >0  # it return tyruth val;ues 
'''
# [[ True False False False]
#  [ True False False False]
#  [False  True  True  True]
#  [False False False False]]
# Traceback (most recent call last):
#   File "c:\Users\Lenovo\Desktop\all python\data science by Wes Mc Kinney\0011_methodBooleanArray.py", line 8, in <module>
#     print(arr>0).sum()   # it count the no of values >0
# AttributeError: 'NoneType' object has no attribute 'sum'

arr_sum = (arr>0).sum()
print(arr_sum)


'''
method 2:~ 
any() ---> check weather one or more val;ue in an array is true 
all() ----> check if every valyuer i strue 
'''
bool = np.array([True,False,True])
print(bool.any())
print(bool.all())

bool_num = np.array([1,2,3,0,0,0,50,500])     # num > 0 == true else false 
print(bool_num.any())
print(bool_num.all())


'''
shorting -------> arr.sort()
'''

arr_sort = np.random.randn(4,4)
print(arr_sort.sort())        # reasult ----> none

arr_sort1d = np.array([10,20,5,2,1,100,500,4,6,9,2])
print(arr_sort1d.sort())      #AttributeError: 'NoneType' object has no attribute 'ndim'
print(arr_sort1d)               # after the sort array is not printed 


'''
multi -D array can have each 1-D array sorted by providing the axis 
'''

arr_multi = np.random.randn(5,3)
arr_multi.sort(1)     # all the y-axis will be sorted 
print(arr_multi)















