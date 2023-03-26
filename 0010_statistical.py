'''

statistical methods 
'''

from cgi import print_arguments
import numpy as np 
arr = np.random.rand(5,4)
print(arr)

print(arr.mean())

print()
print(arr.sum())


#  function like sum and mean have one optioinal axis argument which compute thje stats along the axis (0 ior 1)

print(arr.mean(axis=1))   # along axis 1(vertically)
print(arr.mean(axis = 0))   #$ along axis 0 (horizontallty )


# cumsum() and cumprod() produce an imediate reasult to use 
arr1  = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr1.cumsum(0))               # CUMULATIVE SUM OF ELEMENT STARTING FROM 0
print(arr1.cumprod(1))                #CUMULATIVE SPRODUCT  OF ELEMENT STARTING FROM 1


#[[ 1  2  3]
#  [ 5  7  9]
#  [12 15 18]]

# [[  1   2   6]
#  [  4  20 120]
#  [  7  56 504]]


print(arr1.argmax())        # reaturn the indices of max val 
print(arr1.argmin())         # reaturn the indices of min val 
 
print(arr1.max())                # reaturn the max  element 
print(arr1.min())            # reaturn the min element 


#  std,var calculate  std-dfaviation and std-variance ,with denominator= 1 as defasult 

print(arr1.var(axis=0))   # axis is a optional argumaent 
print(arr1.std(axis=1))


































