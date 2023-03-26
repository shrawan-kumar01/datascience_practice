'''
001. write a python programm to print the environment variable 
'''

import os
# ACCESS ALL ENVIRONMENT VARIABLE 
print("all environment variable")
print(os.environ)
print("\n")

# ACCESS A PARTICULAR ENVIRONMENT VARIABLE 

# print(os.environ['home'])

# print("\n")
# print(os.environ['path'])


#  SAMPLE SOLLUTION TWO 

for data in os.environ:
    print(data)
    print("*" * 50)
    # print(os.environ)
    # print("-"*50)



'''
write a python programm to get current user name 
'''

import getpass
print(getpass.getuser())



'''
write a python programm to get6 current ip address using python's stdlib
'''


import socket
print([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] 
if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), 
s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, 
socket.SOCK_DGRAM)]][0][1]]) if l][0][0])


'''
write a python programm to get height and width of the current coonsole 
'''









