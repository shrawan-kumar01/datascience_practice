'''
programm by w3resources
practice on ing
'''

'''
1. write a PROGRAMM  to print length of a given string
'''
# str = input("enter the string :~ ")
# sollution 1
# print(len(str))
# sollution 2
# length = 0
# for char in str:
#     length = length + 1


# print(length)

#  function based sollution
def str_count(string):
    count = 0
    for char in string:
        count += 1
    return count


string_object = str_count("hi shrawan how are yoy")
print(string_object)

'''
2. write a programm to count the frequency of each character appeared in a string
'''


def char_freq(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict


print(char_freq('google.com'))

#  sollution repetation :-


def fre_char(string2):
    dict2 = {}
    keys = dict2.keys()
    for n in string2:
        if n in keys:
            dict2[n] += 1
        else:
            dict2[n] = 1

    return dict2


print(fre_char('hi i am shrawan'))

'''
 Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.
'''


def get_fst_last(string):
    empt_str1 = ""
    empt_str2 = ""

    if len(string) < 2:
        print("word cant be formed with a single character")

    else:
        for n in string:
            empt_str1 = string[0:2]
            empt_str2 = string[-2:]

        final_string = empt_str1 + empt_str2

    return final_string


get_ele_object = get_fst_last('w3resourczx')
print(get_ele_object)


'''
4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
'''


def get_chartoDoler(string):
    char = string[0]
    str1 = char.replace(char,'$')
    str1  = char + str1[1:] 

    return str1

print(get_chartoDoler('restart'))
