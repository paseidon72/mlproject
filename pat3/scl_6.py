import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# with open('Ames_Housing_Feature_Description.txt', 'r') as f:
#     print(f.read())
df = pd.read_csv('Ames_outliers_removed.csv')
df = df.drop('PID', axis=1)
df = 100 * df.isnull().sum() / len(df)

def percent_missing(my_df):
    result = 100 * my_df.isnull().sum() / len(my_df)
    result = result[result > 0].sort_values()
    return result

# percent_nan = percent_missing(df)
#
# plt.figure(figsize=(7, 3), dpi=200)
# sns.barplot(x=percent_nan.index, y=percent_nan)
# plt.xticks(rotation=90)
# plt.ylim(0, 1)
#
# percent_nan = percent_nan[percent_nan < 1]
# df[df['Electrical'].isnull()]['Garage Area']
# df[df['Bsmt Half Bath'].isnull()]

# df = df.dropna(axis=0, subset=['Electrical', 'Garage Area'])
# percent_nan = percent_missing(df)
# percent_nan = percent_nan[percent_nan < 1]

# bsmt_num_cols = ['BsmtFin SF 1', 'BsmtFin SF 2', 'Bsmt Unf SF', 'Total Bsmt SF',
#                  'Bsmt Full Bath', 'Bsmt Half Bath']
# df[bsmt_num_cols] = df[bsmt_num_cols].fillna(0)
# bsmt_str_cols = ['Bsmt Qual', 'Bsmt Cond', 'Bsmt Exposure', 'BsmtFin Type 1',
#                  'BsmtFin Type 2']
# df[bsmt_str_cols] = df[bsmt_str_cols].fillna('None')
# percent_nan = percent_missing(df)

# df['Mas Vnr Type'] = df['Mas Vnr Type'].fillna('None')
# df['Mas Vnr Area'] = df['Mas Vnr Area'].fillna(0)
# percent_nan = percent_missing(df)

# gar_str_cols = ['Garage Type', 'Garage Finish', 'Garage Qual', 'Garage Cond']
# df[gar_str_cols] = df[gar_str_cols].fillna('None')
# percent_nan = percent_missing(df)

# df['Garage Yr Blt'] = df['Garage Yr Blt'].fillna(0)
# percent_nan = percent_missing(df)

# df = df.drop(['Pool QC', 'Misc Feature', 'Alley', 'Fence'], axis=1)
# percent_nan = percent_missing(df)

df['Fireplace Qu'] = df['Fireplace Qu'].fillna('None')
sns.boxplot(x='Lot Frontage', y='Neighborhood', data=df, orient='h')
df.groupby('Neighborhood')['Lot Frontage'].mean()
df['Lot Frontage'] = df.groupby('Neighborhood')['Lot Frontage'].transform(lambda value: value.fillna(value.mean()))
df['Lot Frontage'].isnull().sum()
df['Lot Frontage'] = df['Lot Frontage'].fillna(0)
df['Lot Frontage'].isnull().sum()
percent_nan = percent_missing(df)

plt.show()
print(percent_nan)
#print(df)
