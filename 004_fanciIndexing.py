"""     fancy indexing """
from cgi import print_arguments
import numpy as np 


#  fancig indexing describe indexing using integer array 

arr = np.empty((8,4))
# print(arr)
# for i in range(8):
#     arr[i] = i

# print(arr)

#  selecting subset of row in a particular order 
# arr[[1,2,3,4]]                      #[1. 1. 1. 1.]
                                    # [2. 2. 2. 2.]
                                    # [3. 3. 3. 3.]
                                    # [4. 4. 4. 4.]
                                    # [5. 5. 5. 5.]
                                    # [6. 6. 6. 6.]
                                    # [7. 7. 7. 7.]]
# print(arr)

#  NEGATIVE INDICES SELECT ROW FROM END 


print(arr[[-3,-5,-7]])

'''
passing multiple indices array :~   select 1-d array of element corresponding to each touple of the indices 
'''

arr_ = np.arange(32).reshape((8,4))
# print(arr_)

print(arr_[[1,5,7,2],[0,3,1,2]])         # the element here selected is (1,0),(5,3),(7,1),(2,2)

"""
another way:~
use np.ix_ function which convert two 10d array in an indexer that select the square region 
"""
print("*"*50)

# print(np.ix_[arr_[[1,5,7,2],[0,3,1,2]]])      #TypeError: 'function' object is not subscriptable
arr_squre = arr[np.ix_([1,5,7,2],[0,3,1,2])]     # it printing an empity array 
print(arr_squre)

'''
fanci indexing always copies the data into a  new array 
'''













