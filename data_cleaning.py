# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 11:56:50 2020

@author: pc
"""

import pandas as pd

df = pd.read_csv('ds_jobs.csv')

# parse salary: remove parentheses and '(Glassdoor est.)' from salary est.

df = df[df['Salary Estimate'] != '-1']
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_Kd = salary.apply(lambda x: x.replace('K','').replace('$',''))

df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['employer_provided_salary'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0)

minus_hr = minus_Kd.apply(lambda x: x.lower().replace('per hour','').replace('employer provided salary:',''))

df['min_salary'] = minus_hr.apply(lambda x: int(x.split('-')[0]))

df['max_salary'] = minus_hr.apply(lambda x: int(x.split('-')[1]))

df['avg salary'] = (df.min_salary+df.max_salary)/2


# company name text only

df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] < 0 else x['Company Name'][:-3], axis = 1)

# state field

df['job_state'] = df['Location'].str.split(',').str[1]
df.job_state.value_counts()

df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis = 1)

# age of company

df['age'] = df.Founded.apply(lambda x: x if x < 1 else 2020 - x)

# parse job description

df['Job Description']

#Python
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)

#r-studio
df['R_yn'] = df['Job Description'].apply(lambda x: 1 if 'r-studio' in x.lower() else 0)

#spark
df['spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)

#aws
df['aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)

#excel
df['excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)

#To check which columns might need to be dropped
df.columns

df_clean = df

df_clean.to_csv('ds_salary_clean.csv', index = False)

