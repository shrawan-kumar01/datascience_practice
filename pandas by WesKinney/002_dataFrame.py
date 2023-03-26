
'''
pandas data frame 
datat is stored in 2-d array in data frame 
'''
from cgi import print_arguments
from pickle import POP
from sre_parse import State
import pandas as pd 
data = {"state":['bihar','up','rajst','madrash'],
        "year":[2005,2006,2009,2008],
        "pop":[1.5,1.4,1.3,8.6]} 


frame = pd.DataFrame(data)
print(frame)
frame_column = pd.DataFrame(frame,columns=['STATE',"YEAR","POP"])
print(frame_column)

#    STATE  YEAR  POP
# 0    NaN   NaN  NaN
# 1    NaN   NaN  NaN
# 2    NaN   NaN  NaN
# 3    NaN   NaN  NaN
print("*"*100)
frame3_column = pd.DataFrame(data,columns=['STATE',"YEAR","POP"])
print(frame3_column)
# Empty DataFrame
# Columns: [STATE, YEAR, POP]
# # Index: []

frame4_column = pd.DataFrame(data,columns=['STATE',"YEAR","POP"],index=['one','two','three','four'])
# print(frame4_column)
#       STATE YEAR  POP
# one     NaN  NaN  NaN
# two     NaN  NaN  NaN
# three   NaN  NaN  NaN
# four    NaN  NaN  NaN
print(frame4_column.columns)
# print(frame['state'])
# 0      bihar
# 1         up
# 2      rajst
# 3    madrash

print(frame['pop'])
print(frame['year'])


'''
retrivuibg the row by ix[row name]  --- > method
'''
print(frame)
# frame_ix =frame.ix[' 2']            #AttributeError: 'DataFrame' object has no attribute 'ix'
# print(frame_ix)    

'''
insewrting a values as a series in a data frame 
'''

print(frame)
values = pd.Series([-1.2,-1.3], index=[0,3])
frame['debt'] = values
print(frame)

frame['country'] = frame.state == 'bihar'
print(frame)
print(frame.T)
#   + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
    # + FullyQualifiedErrorId : AmpersandNotAllowed 





















