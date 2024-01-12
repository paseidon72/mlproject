import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# with open('Ames_Housing_Feature_Description.txt', 'r') as f:
#     print(f.read())

df = pd.read_csv('Ames_NO_Missing_Data.csv')
# df = df.isnull().sum()
# df = df.isnull().sum() > 0
df['MS SubClass'] = df['MS SubClass'].apply(str)

# direction = pd.Series(['Up', 'Up', 'Down'])
# direction = pd.get_dummies(direction, drop_first=True)

my_object_df = df.select_dtypes(include='object')
my_numeric_df = df.select_dtypes(exclude='object')
df_objects_dummies = pd.get_dummies(my_object_df, drop_first=True)
final_df = pd.concat([my_numeric_df, df_objects_dummies], axis=1)


print(final_df)
#print(df_objects_dummies)
#print(my_object_df)
#print(df)
#print(direction)
