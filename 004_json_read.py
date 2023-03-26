'''
reading json data using pandas 
'''

from cgi import print_arguments
import pandas as pd 
data_json = pd.read_json("json_data.json")
print(data_json.to_string())
print

'''
JSON == python dict
If your JSON code is not in a file, but in a Python Dictionary, you can load it into a DataFrame directly:
'''

#   LOAD A PYTHON DICTONARIES INTO A DATA FRAME 

data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

dict_load = pd.DataFrame(data)
print(dict_load)