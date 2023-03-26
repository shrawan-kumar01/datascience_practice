import numpy as np 
arr1 = np.arange(5).reshape(1,5)
print(arr1)

arr1_square = np.square(arr1)
print(arr1_square)


#  exp :---- > compute the e^x of each element 
arr1_exp = np.exp(arr1)
print(arr1_exp)

# log :---- > base e

arr1_log10 = np.log(arr1)
print(arr1_log10)   # RuntimeWarning: divide by zero encountered in log
                    # arr1_log10 = np.log(arr1)
                    # [[      -inf 0.         0.69314718 1.09861229 1.38629436]]

# log10
arr1_log101 = np.log10(arr1)
print(arr1_log101)
# log2
arr1_log2 = np.log2(arr1)
print(arr1_log2)
# log1p :-----> log(1+x)
arr1_log1p = np.log1p(arr1)
print(arr1_log1p)


#  sign :-----> compute the sign of each element 1,0,-1
arr1_sign = np.sign(arr1)
print(arr1_sign)

#  ceil :----> the smallest integer grater than or equal to each element 

arr1_ceil = np.ceil(arr1)
print(arr1_ceil)

# floor :---> compute tyhe floor of each element >>> the largest integer less than or equal to each element 

arr1_floor = np.floor(arr1)
print(arr1_floor)


