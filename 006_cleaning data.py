'''
cleaning data 

Empty cells
Data in wrong format
Wrong data
Duplicates
'''


#   REMOVING ENPITY CELL : WE CAN REMOVE ENTIRE ROW AS DATA IS VERY BIG IT WILL NOT EFFECT THE REASULT 

'''
REMOVE ROWS 
'''

import pandas as pd 

df  = pd.read_csv("data.csv")
print()
new_df = df.dropna()
# print(new_df.to_string())
# print(df.info())
print("*"*20)
# print(new_df.info())
#  By default, the dropna() method returns a new DataFrame, and will not change the original

df.dropna(inplace=True)   # it change the existing data  and remove all the null rows and return the same data frame 
print(df.info())


'''
replace empity values 
'''

df.fillna(13000000, inplace=True)
print(df.to_string())




