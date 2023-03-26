'''
every array having 
1. a touple ===  size 
2. dtyep = data type 
3. dimension 
array is an ndarray object in numpy 

'''


from cgi import print_arguments, print_directory
import numpy as np 
data = np.arange(20)
data_2 = np.array([1,2,3,4,5,6])
data_3 = np.array([[1,2,3,4,5,6,7,8,9],[10,20,30,40,50,60,70,80,90]])
print(data_3)
print(data_2)
print(data)
print(data_3.ndim)
print(data_3.shape)
print
print(data_3.tobytes)        #<built-in method tobytes of numpy.ndarray object at 0x0000023BB2CB1F50>

print(type(data_3))     
print(data_3.dtype)              # data type is stored in special dtype object 

print(np.zeros(10))
# print(np.zeros(2,3))       TypeError: Cannot interpret '3' as a data type
print(np.zeros((2,3)))       # (2,3) a tuple defining the size of array 
print(np.empty((2,3,2)))            # iot not always zeros value it reatuen uninitilised garbeg value 
print()

'''
is dtype is not set in nd array the defaylty dtype = float64
'''
eye_array = np.eye(300,300)
# print(eye_array.tostring)    #<built-in method tostring of numpy.ndarray object at 0x000001D9D4D2C990>

t_array = np.array([1,2,3,4,5,67,8,9], dtype=np.float16)        # np.dtupe ha no attribute like float128
print(t_array.dtype)

'''
Casting an Array into different datatype using (astype) ------> method
'''
c_array = np.array([1,2,3,4,5,6],dtype=np.int64)
print(c_array.dtype)
casted_array = c_array.astype(np.float64)      # change the d-type
print(casted_array.dtype)
#  CASTING FLOAT TO INTEGER IT MAY LOSE OF DATA :~ METHOD TYO BE USED IS  :~~~~ astype(np.int64)

'''
converting a string to a integer type using astype method 
'''

str_arr = np.array(["1","2","3","4"],dtype = np.string_)   #dtype = np.string     : reasult :----> |S1
print(str_arr)
print(str_arr.dtype)           # reasult without dtype = np.string  :-------  <U1
int_str_array = str_arr.astype(np.int64)
print(int_str_array)
print(int_str_array.dtype)

"""
1.  calling astupe() always create a new array even if dtype is same in both the case 
2.  numpy is intelegent enough to match its type to dtype in case int ==== intp[intrepreter type]
"""

'''
another array's datatype attribute 
'''
int_arr1 = np.arange(10)
caliber = np.array([1.1,2.2,.3,4.1],dtype=float)    # matched dtype to float64 automatically 
print(caliber.dtype)

int_arr1.astype(caliber.dtype)
print(int_arr1.dtype)







































