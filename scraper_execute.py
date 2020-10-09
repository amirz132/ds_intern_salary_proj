# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 07:38:37 2020

@author: pc
"""

import web_scraper_glassdoor as gs
import pandas as pd

path = "C:/Users/pc/Documents/ds_intern_salary_proj/chromedriver_win32/chromedriver.exe"

df = gs.get_jobs('data scientist intern',200,False,path,15)

df.to_csv('ds_jobs.csv',index = False)