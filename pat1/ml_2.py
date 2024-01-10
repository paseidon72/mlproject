import pandas as pd

"""Создание обьекта Series"""
# myindex = ['USA', 'CANADA', 'MEXICO']
# mydata = [1776, 1867, 1821]
# myser = pd.Series(data=mydata, index=myindex)
# print(myser)
# ages = {'Sam': 5, 'Frank': 10, 'Spike': 7}
# ages1 = pd.Series(ages)
# print(ages1)
"""Операции над обьектом Series"""
q1 = {'Japan': 80, 'China': 450, 'India': 200, 'USA': 250}
q2 = {'Brasil': 100, 'China': 500, 'India': 210, 'USA': 260}
sel1 = pd.Series(q1)
sel2 = pd.Series(q2)
# print(sel1.keys())
# print(sel1)
# print(sel1['USA'])
ver1 = sel1 * 2
ver2 = sel1 / 100
# print(ver1)
# print(ver2)
ver3 = sel1.add(sel2, fill_value=0)
print(ver3)