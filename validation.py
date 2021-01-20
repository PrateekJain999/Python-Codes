# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 21:08:02 2019

@author: yogesh
"""
import re

str = "hi, am yogesh kumar and 28 year old.i yogesh kumar yogesh kumar"
"""x = re.search("\d", str)
print(x)
print("The first white-space character is located in position:", x.start())""" 
"""x = re.split(",", str)
print(x)
x = re.split("\s", str, 2)
print(x)
x = re.sub("kumar", "mehra", str)
print(x)

x = re.sub("kumar", "mehra", str,2)
print(x)"""
x = re.search(r"\by\w+3", str)
print(x.group())