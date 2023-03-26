'''
ADDING REMOVING AND SORTING ELEMENT IN NUMPY 
'''

import numpy as np 

arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
print(np.sort(arr))
print(np.argsort(arr))
# print(np.lexsort(arr))
# print(np.searchsorted(arr))
# print(np.partition(arr))


"""concanating the aary"""

a = np.array([1,2,3])
b = np.array([10,20,30])
c  =np.concatenate((a,b))
print(c)

x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6],[10,30]])

z = np.concatenate((x,y),axis=1)
print(z)
print("spliting of an array in sub array ")

z_split = np.array_split(z,5)
print(z_split)



Arr = np.arange(25)
Arr_split = np.split(Arr,5)
print(Arr_split)

'''
hsplit , vsplit , dsplit  
'''

arr2 = np.array([[[10,20,30],[30,40,50],[60,70,80]],[[10,20,30],[30,40,50],[60,70,80]]])
print(arr2.ndim)
arr2_hsplit = np.hsplit(arr2,1)
print(arr2_hsplit)


x1 = np.arange(8.0).reshape(2,2,2)
print(x1)
x1_hsplit = np.hsplit(x1,2)
print(x1_hsplit)
x1_vsplit =np.vsplit(x1,2) 
print(x1_vsplit)

x1_dsplit = np.dsplit(x1,2)
print(x1_dsplit)







