'''
EXPRESSING THE CONDITIONAL LOGIC AS AN ARRAY OPERATION 
numpy.where ----> fxn is a vactorised verson of ternary expression  x if condition else y
'''


#  problem : take the value from x if corresponding conditionm is true else take from y 


#  method 1:- list comprehension 
from cgi import print_arguments
from tkinter import Y
import numpy as np 
xarr = np.array([1.1,1.2,1.3,1.4,1.5,1.6])
yarr = np.array([2.1,2.2,2.3,2.4,2.5,2.6])
cond = np.array([True,False,True,False,True,False])
reasult = [(x if c else y)                  # list comprihension 
    for x,y,c in zip(xarr,yarr,cond)]

print(reasult)


# method 2:~ np.where()    \# it accept multidimensional array 
result_where = np.where(cond,xarr,yarr)
print(result_where)


#  np.where is used to produce new array of value bgased on anothe r array 

arr_val = np.random.randn(4,4)
print(arr_val)
arr_where = np.where(arr_val >0 ,2,-2)
print(arr_where)

#  set onl;y +ve value to 2 

arr_wh_positive = np.where(arr_val>0,2,arr_val)
print(arr_wh_positive)
# arr_wh_positive = np.where(arr_val>0,2)      # ValueError: either both or neither of x and y should be given




















