# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 23:34:37 2022

@author: Lenovo
"""
from matplotlib import pyplot as plt 
years = [1950,1960,1970,1980,]
gdp = [300.2,543.5,1075,286.2]
plt.plot(years,gdp,color = "red",linestyle = "solid")
plt.title("normal gdp")
plt.ylabel("billion")
plt.xlabel("years")
plt.show()