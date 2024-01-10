import numpy as np
import pandas as pd

"""Обработка текста"""

# name = pd.Series(['andrew', 'bobo', 'claire', 'david', '5'])
# name = name.str.upper()
# tech_finance = ['GOOG, APPL, AMZN', 'JPN, BAC, GS']
# name = pd.Series(tech_finance)
#name = name.str.split(',')
#name = name.str.split(',').str[0]
#name = name.str.split(',', expand=True)
name = pd.Series(['andrew  ', 'bo:bo', '  claire  '])
#name = name.str.replace(':', '')
#name = name.str.replace(':', '').str.strip()
name = name.str.replace(':', '').str.strip().str.capitalize()
# def cleanup(name):
#     name = name.str.replace(':', '')
#     name = name.str.strip()
#     name = name.str.capitalize()
#     return name
#
# name = name.apply(cleanup)

print(name)