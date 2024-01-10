import pandas as pd
import numpy as np

"""Сводние таблици"""

df = pd.read_csv('Sales_Funnel_CRM.csv')
# licenses = df[['Company', 'Product', 'Licenses']]
# licenses = pd.pivot(data=licenses, index='Company', columns='Product', values='Licenses')
#df = pd.pivot_table(df, index='Company', aggfunc='sum')
#df = pd.pivot_table(df, index='Company', aggfunc='sum', values=['Licenses', 'Sale Price'])
#df = pd.pivot_table(df, index=['Account Manager', 'Contact'], values=['Sale Price'], aggfunc='sum')
df = pd.pivot_table(df, index=['Account Manager', 'Contact'], values=['Sale Price'], columns=['Product'], aggfunc='sum')
print(df)