"""
LOAD FILE TO OUR DATA FRAME  
 CSV ===== COMMA SEPERATED FILE

"""

import pandas as pd 
file = pd.read_csv("data.csv")
# print(file.to_string())

# Tip: use to_string() to print the entire DataFrame

print("without to_string() method " + "*"*10)
# print(file)   # it prit first 5 row and last five row 


print(pd.options.display.max_rows)


# In my system the number is 60, which means that if the DataFrame contains more than 60 rows, the print(df) statement will return only the headers and the first and last 5 rows


'''
change the limit on maximum row 
'''

pd.options.display.max_column = 1000
print(pd.options.display.max_column)
print(file)

