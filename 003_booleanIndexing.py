'''
BOOLEAN INDEXING : ----
'''

# from unicodedata import name
from cgi import print_arguments
import numpy as np 

names = np.array(["bob","will","sanjuu","dsojii","will","ask","will","abs","will"])
# data = np.random(9,4)
data = np.random.rand(9,4)
print(names)
print(data)
print(names == "will")
print(data[data<0])

# print(data[names=="will",2:1:])

# print(data[names=="will",3])

# print(names != "will")         # alter the condition 

#  pritnting the same things yusing negative of the condition using (-)

print(-data[names == "will",3])


"""
                    python keyword AND / OR  do not work with  BOOLEAN  arrays.
"""


#  integerate two boolean arithmatic operation at onse 

boo_ope = (names == "will") | (names== "sanjana")
print(boo_ope)                   #[False  True False False  True False  True False  True]

"""
                    selecting data by boolean indexing always create a new copy of the array even if the returned array ius unchanged 
"""




"""
setting all the valuers in the boolean array 
"""
# data[data>0] = 0
# print(data


# data[names == "will"] = 70000
# print(data)








'''set_bool_val = data[data <0 ==0 ].all()         #ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
print(set_bool_val)
'''



































'''
arr = np.random.randint(low=10,high=100,size=20).reshape(4,5)
print(arr)
print(arr>50)
print(arr[arr>50])

'''




