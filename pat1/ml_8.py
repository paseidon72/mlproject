import numpy as np
import pandas as pd

"""Обьединене дата фреймов"""

# data_one = {'A': ['A0', 'A1', 'A2', 'A3'], 'B': ['B0', 'B1', 'B2', 'B3']}
# data_two = {'C': ['C0', 'C1', 'C2', 'C3'], 'D': ['D0', 'D1', 'D2', 'D3']}
# one = pd.DataFrame(data_one)
# two = pd.DataFrame(data_two)
# #df = pd.concat([one, two], axis=1)
# two.columns = one.columns
# df = pd.concat([one, two], axis=0)
# df.index = range(len(df))
registration = pd.DataFrame({'reg_id': [1, 2, 3, 4], 'name': ['Andrew', 'Bobo', 'Claire', 'David']})
logins = pd.DataFrame({'log_id': [1, 2, 3, 4], 'name': ['Xavier', 'Andrew', 'Yolanda', 'Bobo']})
#df = pd.merge(registration, logins, how='inner', on='name')
#df = pd.merge(left=registration, right=logins, how='left', on='name')
#df = pd.merge(left=registration, right=logins, how='right', on='name')
#df = pd.merge(registration, logins, how='outer', on='name')
registration = registration.set_index('name')
#df = pd.merge(registration, logins, left_index=True, right_on='name', how='inner')
registration = registration.reset_index()
registration.columns = ['reg_name', 'reg_id']
# df = pd.merge(registration, logins, how='inner', left_on='reg_name', right_on='name')
# df = df.drop('reg_name', axis=1)
registration.columns = ['name', 'id']
logins.columns = ['id', 'name']
#df = pd.merge(registration, logins, how='inner', on='name')
df = pd.merge(registration, logins, how='inner', on='name', suffixes=('_reg', '_log'))
print(df)