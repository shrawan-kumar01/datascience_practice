'''
practice set on     JSON     


'''

'''
1. write a python programm to converyt JSON data to a python object.
'''

import json 
json_object = '{"name":"devid","class":"12","age":10}'
python_object = json.loads(json_object)    # json.loads convert the json data int to python data type like list and list is a python object 


print(python_object)
print(json_object)
print("name" , python_object["name"])
print("class", python_object["class"])
print("age", python_object["age"])

print
print
print

'''
2. write a programm to convert python object to json data 
'''

pyt_obj = {"a":1,"b":2,"c":3,"d":4}
print(type(pyt_obj))
json_obj = json.dumps(pyt_obj) # reasult is json string 
print(type(json_obj))
print(json_obj)



'''
3. write a python program to convert a python object to json striung and print all the values 
'''

python_list = ["ram","mohan","shyam"]
python_str = "shrawan kumar"
python_int = 10
python_flt= 10.01
python_dict = {"ab":10,"bc":20,"cd":30,"de":40}
json_list = json.dumps(python_list)
json_str = json.dumps(python_str)
json_int = json.dumps(python_int)
json_dict = json.dumps(python_dict)
json_flt = json.dumps(python_flt)

print(json_dict)
print(type(json_dict))


'''
4. Write a Python program to convert Python dictionary object (sort by key) to JSON data. Print the object members with indent level 4
'''

python_dictonarie = {"abc":100,"bcd":200,"cde":300,"def":400}
print(type(python_dictonarie))
json_dictonaries = json.dumps(python_dictonarie,sort_keys = True , indent=40)
print
print(json_dictonaries)
print(type(json_dictonaries))

'''
5. write a python programm to convert json encoded data iin to a  pyrthon object 
'''

'''
6. write a python programm to create a JSON NEW FILE FROM AN EXISTING JSON FILE 

'''





























	