from audioop import add
import numpy as np 
print(np.__version__)
print(np.__git_version__)  #1.22.3
# 7d4349e332fcba2bc3f266267421531b3ec5d3e6

# print(np.show_config)  #<function show at 0x000001DBF7BF8280>

# print(np.show_config())

'''
2. write a programm to get help on add function 
'''
print()
# print(np.info(add()))

# print(np.info(np.add))

'''
3. Write a NumPy program to test whether none of the elements of a given array is zero
'''
arr =np.array([1,2,3,0,1,58,56,10,0])
print(np.all(arr))
print(np.any(arr))

'''
3.Write a NumPy program to test whether any of the elements of a given array is non-zero
'''

arr_any = np.array([1,2,3,0,0,0,0])
arr_all = np.array([1,2,3,4,5,6])
print(np.any(arr_any))
print(np.all(arr_all))

#  any() --- non zero element found --> true
#  all()---- non zero element not found ---> false

'''
5. Write a NumPy program to test a given array element-wise for finiteness (not infinity or not a Number)
'''


























