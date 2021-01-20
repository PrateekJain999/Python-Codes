# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 12:34:56 2019

@author: yogesh
"""

import pandas as pd
csv_file = r'C:\Users\yogesh\AppData\Local\Programs\Python\Python37-32\sonu.xlsx'
movies = pd.read_excel(csv_file)
print(movies["SrNo"])
