# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 23:46:14 2022

@author: Lenovo
"""
from matplotlib import pyplot as plt 
movies = ["a","b","c","d","e","f"]
ratting = [5,10,8,3,1.1,4]
plt.bar(movies,ratting,color = "blue",linestyle = "solid")
plt.ylabel("movies")
plt.xlabel("ratting",)
plt.title("movuie ratting ")
plt.show()
