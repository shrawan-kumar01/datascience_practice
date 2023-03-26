'''
it is a fast element wise operation 
1.       binary ufunc ---- > single argument : element wise operation 
2.       uinary ufunc ---- > take two array as argument and return :         asingle array 
'''
import numpy as np 
arr = np.arange(20)
arr_sqrt = np.sqrt(arr)
print(arr_sqrt)

arr_exp = np.exp(arr)
print(arr_exp)


# unary ufunc 

x = np.array([1,100,3,4,5,600])
y = np.array([10,220,30,405,50,60])
print(f"{x} anddfxvfhbsdfhsr {y}")

xy_maximum = np.maximum(x,y)   # check all the element of both the array and pritn the max from either of array 
print() 
print(xy_maximum)
print()
xy_add = np.add(x,y)
print(xy_add)

'''
while not all ufunc , .modf ---> a vectorised verson of built in python divmod
.modf ---> reaturn value === integer part and floating part 
'''

arr_dmod = np.random.randn(7) * 5
arr_modf = np.modf(arr_dmod)
print(arr_modf)             #(array([ 0.67122246, -0.32141608,  0.85834394,  0.2038297 , -0.15753615,
                            #-0.04501303,  0.9972484 ]), array([  9.,  -2.,   7.,   7.,  -5., -11., 



'''
important universal function :------>  unary ufunc
'''

#  abs ,fabs : compute absolute values 
arr1 = np.array([-1.0,2.0,-5,10])
arr_abs = np.abs(arr1)
print(arr_abs)

# sqrt : calculate squre root 

arr_sqrt2 = np.sqrt(arr1)               #[       nan 1.41421356        nan 3.16227766] nan for complex number 
# print(arr_sqrt2)
# arr1_sq = np.square(arr1)
# print(arr1_sq)























