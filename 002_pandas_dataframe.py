'''
a pandas data frame isn a 2-d  data strcture m, like a 2-d array or a table with rows and column 
'''

#  CREATE A SAMPLE DATA FRAME 
import pandas as pd 

my_data = {
    "calories": [300,600,900],
    "time": [30,60,90],
    "implse":[3000,6000,900],
    "h_pressuer":[3.0,6.0,9.0],
    "face_value": [20,50,80]
}
#  load a data into a data frame object of pandas 
my_data_frame = pd.DataFrame(my_data)
print(my_data_frame)


# LOCATE ROW 

#  PANDAS USES loc attribute tio reaturn A SEPECIFIC ROW 

print(my_data_frame.loc[0])
print(my_data_frame.loc[1])   # it rteatuern the pandas seriesd 
print(my_data_frame.loc[2])
# print(my_data_frame.loc[3])   # throes an error 


#  reaturn multiple rows 
print("*"*50)
print(my_data_frame.loc[[0,1]])    # double [[]] loc[], index[]


'''
Note: When using [], the result is a Pandas DataFrame.
'''



'''
    NAMED INDEXES
    With the index argument, you can name your own indexes
'''


data_indexed = pd.DataFrame(my_data,index=["day1","day2","day3","day4"])
print(data_indexed)




