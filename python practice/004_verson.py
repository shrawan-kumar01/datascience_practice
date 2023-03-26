'''
write a programm to get python version u r using.

'''

from distutils import extension
from doctest import Example
import sys
print("system version \n ")
print(sys.version)

print

print(sys.version_info)
 

'''
 write a programm to display date and time

'''
import datetime
now = datetime.datetime.now()
print
print("current date and time is :~  ")
# print(now.strftime("%y-%m-%d %h-%m-%s"))     # value error 
print(now.strftime("%Y-%M-%d %H:%M:%S"))     # value error 


'''
WRITE A PROGRAMM TO FIND AREA 
'''
# R = eval(input("enter the radious :~  "))
# area = 3.14 * R*R
# print(area)

'''
write a programm to which accept the users first and last name and print thamn in reverse order with a space in between them '''

# fst_name = eval(input("enter the bfirst name :~  "))
# lst_name = eval(input("enter the last name :~ "))
# print(f"{lst_name} {fst_name}")

'''
write a programm  which accept a sequence of commma se-perated number from user and generate a list and touple with those number 
'''
print

# a = input("enter the number :~")
# list = a.split(',')
# tuple = tuple(list)
# print('list : ',list)
# print('tuple: ',tuple)

'''
write a programm to accept a file name from the user and print the entension of that file 
'''
"""WRONG , HOW COMPUTER WILL KNOW """

# file_name = input("enter the file name :~  ")
# extension = list()
# for char in file_name:
#     if char == '.':
#         extension.add(char)
#         char += 1
#         print(extension)


#   str.rsplit(sep=None, maxsplit=-1) function
# The function returns a list of the words of a given string using a separator as the delimiter string.

# If maxsplit is given, the list will have at most maxsplit+1 elements.
# If maxsplit is not specified or -1, then there is no limit on the number of splits.
# If sep is given, consecutive delimiters are not grouped together and are deemed to delimit empty strings.
# The sep argument may consist of multiple characters.
# Splitting an empty string with a specified separator returns [''].

# file_name = input("enter the file name :~  ")
# f_extent = file_name.split('.')
# print("extension of the file name is: ~ " + repr(f_extent[+1]))

'''
write a programm to display first amnd last color name froim the given list :
color_list = ["Red","Green","White" ,"Black"]
'''

color_list = ["Red","Green","White" ,"Black"]
print(color_list[0])
print(color_list[-1])

print("%s %s" %(color_list[0] , color_list[-1]))


'''
 Write a Python program to display the examination schedule. (extract the date from exam_st_date). Go to the editor
exam_st_date = (11, 12, 2014)
'''
'''
#   WRONG 

exam_st_date = ['11', '12', '2014']
for item in exam_st_date:
    exam_st_date= exam_st_date.replace(exam_st_date.split(','),'/') 

    print('yourb exam start in : ~ ',exam_st_date)

'''

exam_st_date = (11,12,2014)
print("your exam will start from : - %i / %i /%i "%(exam_st_date))


'''
10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn
'''

# num = int(input("enter the number :~  "))
# num1 = int("%s" %(num))
# num2 = int("%s%s" %(num , num))
# num3 = int("%s%s%s" %(num, num, num))
# res = num1  + num2 + num3
# print(res)


'''
11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
Sample function : abs()
'''


print(abs.__doc__)  # reaturn the absolute value of the argument 

'''
12. Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' modul'''

'''
NOTE:~~~~~~
calendar.month(theyear, themonth, w=0, l=0):

The function returns a month’s calendar in a multi-line string using the formatmonth() of the TextCalendar class.

'I' specifies the number of lines that each week will use
'''

import calendar

# yyyy = int(input("enter the year:~ \n "))
# mm = int(input("enter the month :~  \n"))
# print(calendar.month(yyyy,mm))

'''
13. Write a Python program to print the following 'here document'. Go to the editor
Sample string :
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example
'''

print("""a string that you ""don''t"" have the following ''here \n document'' \n this \n is a .......... multi-line \n 
heredoc \n string ...............>Example""")
