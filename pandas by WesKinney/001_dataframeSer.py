from operator import index
from sre_parse import State
import numpy as np 
import pandas as pd
from pandas import Series,DataFrame 

obj = Series([4,5,-1,8])
print(obj)
print(obj.values)
print(obj.index)             #RangeIndex(start=0, stop=4, step=1)

'''
data piont wit index 
'''
obj_index = Series([4,5,-1,8],index=['a','b','c','d'])
print(obj_index)
print(obj_index.index)          #Index(['a', 'b', 'c', 'd'], dtype='object')
print(obj_index.values)

print(obj_index['d'])
print(obj_index[['d','a']])

'''
mathematical operation is preserved in pd.series
'''
print(obj_index <0)
print(obj_index > 0)
# dtype: bool
# a     True
# b     True
# c    False
# d     True
print(obj_index *10)
print(np.exp(obj_index))

'''
series is a maping of index value to data value 
'''
print('b' in obj_index)
print(8 in obj_index)     # False  : scince it check for assigned index 
print('e' in obj_index)

'''
data series cab be created by passing dict - python 
'''
dict = {
    'name':['ram','shyam','shankar'],
    'phone number':[123,456,789],
    'email':['ram@gmail.com','shyam@gmail.com','shankar@gmail.com']
}

dict_series = Series(dict)
print(dict_series)

dict_state = ['bihar','mathura','hiumalaya']
dict_ind_state = Series(dict_series,index=dict_state)
print(dict_ind_state)
sdata = {'ohi':3500,'taxas':5200,'oregon':1600,'utah':1500}
object1 = Series(sdata)
print(sdata)
states = ['ohi','taxas','califor','mohan nagar']
sdata_indexed = Series(sdata , index= states)
print(sdata_indexed)

# ohi            3500.0
# taxas          5200.0
# califor           NaN
# mohan nagar       NaN
# dtype: float64


print(pd.isnull(dict))          #False
print(pd.isnull(sdata))         #False
object2 = pd.isnull(Series(sdata))
                                    # ohi       False
                                    # taxas     False
                                    # oregon    False
                                    # utah      False
                                    # dtype: bool





print(pd.notnull(Series(sdata)))            #ohi       True
                                            # taxas     True
                                            # oregon    True
                                            # utah      True
                                            # dtype: bool

print("*" *50)
print()

object3 = object1 + object2
print(object3)

'''
name attribute 
'''
object1.name = "kailash perwat"        #Name: kailash perwat, dtype: int64
print(object1)











































