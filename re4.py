# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 20:58:17 2019

@author: yogesh
"""
str="12yogesh kumarc3"
searchObj = re.search( '[a-z]', str, re.M|re.I)
if searchObj:
   print "search --> searchObj.group() : ", searchObj.group()
else:
   print "Nothing found!!"