''' 
    creating the pandas seriez using python object 
'''
from cgi import print_arguments
from re import X
import pandas as pd

a = [1,2,3]
ps_series = pd.Series(a ,index=["x","y","z"])  # each element is indexed with x,y,z respectively 
print(ps_series)
print(ps_series[0])   # call a element by index no 
print(ps_series)
print(ps_series["x"]) # calli g a value with the help of index provided 

"""
KEY VALUE OBJECT AS A SERIES
IT CONVERT A DICTONARIES INTO TO PAndas series 

KEY BECAME THE LABLE 
"""

DICT = {"A":1,"B":12,"C":3}
DICT_SERIES = pd.Series(DICT)
print(DICT_SERIES)
print(DICT_SERIES.keys)
print(DICT_SERIES.values)


# To select only some of the items in the dictionary, use the index argument and specify only the items you want to include in the Serie


dict_series = pd.Series(DICT, index = ["B","c"])
print
print(dict_series)
print(type(dict_series))
print(type(DICT))
print()


'''
DataFrames
Data sets in Pandas are usually multi-dimensional tables, called DataFrames.

Series is like a column, a DataFrame is the whole table
'''


#  creating a data frame in opandas 


my_data  = {
    "calories": [900,600,300],
    "duration": [90,60,30]
}

my_data_frame = pd.DataFrame(my_data)
print(my_data_frame)





