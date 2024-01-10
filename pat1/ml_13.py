import pandas as pd

"""чтение xlsx"""

#df = pd.read_excel('my_excel_file.xlsx')
# df = pd.read_excel('my_excel_file.xlsx', sheet_name='First_Sheet')
# df1 = pd.ExcelFile('my_excel_file.xlsx')
# df2 = df1.sheet_names
sheet_dict = pd.read_excel('my_excel_file.xlsx', sheet_name=None)
df3 = sheet_dict['First_Sheet']
df4 = df3.to_excel('file.xlsx', sheet_name='First_Sheet', index=False)
print(df4)