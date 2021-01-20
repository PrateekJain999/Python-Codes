# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 20:11:44 2019

@author: yogesh
"""

import re

line = "hi This is yogesh mehra";

matchObj = re.match( r'mehra', line, re.M|re.I)
if matchObj:
   print ("match --> matchObj.group() : ", matchObj.group())
else:
   print ("No match!!")

searchObj = re.search( r'mehra', line, re.M|re.I)
if searchObj:
   print ("search --> searchObj.group() : ", searchObj.group())
else:
   print ("Nothing found!!")