'''
ANALYSING THE DATA FRAME 

head() method 
'''

import pandas as pd 

my_data = pd.read_csv("data.csv")
# print(my_data.head(20))

print("information about data ")
print(my_data.info())
# print(my_data.tail(10))

'''
Empty values, or Null values, can be bad when analyzing data, and you should consider removing rows with empty values. This is a step towards what is called cleaning data, and you will learn more about that in the next chapters.


'''