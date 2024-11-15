from unicodedata import numeric

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

cars = pd.read_csv('D:\\mysask\\AI\\mtcars.csv')
cars.columns = ['car_names','mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']
print(cars.head())
print('-' * 100)
print(cars.sum()) #axis = 0 is default
print('-' * 100)
print(cars.sum(axis = 1))

# print(cars.describe())
# print('-' * 100)
# cars_group1 = cars.groupby(cars['cyl'])
# print(cars_group1.describe()) # describe is powerful tool, check the output
# print('-' * 100)
# print(cars_group1.mean(numeric_only = True))
# print('-' * 100)
# print(cars_group1.max())
# print(cars_group1.min())
# print(cars_group1.sum())
# print(cars_group1.count())
# print(cars_group1.std(numeric_only = True))
# print(cars_group1.var(numeric_only = True))
# print(cars_group1.nth(0))

# sales = pd.read_csv('D:\\mysask\\AI\\sales_data.csv')
# sales.columns = ['Date','Region','Product','Sales','Unit']
# print(sales.head())
# print('-' * 100)
# group1 = sales.groupby(by='Region')
# print(group1['Sales'].sum())
# print('-' * 100)
# group2 = sales.groupby(by=['Region','Product'])
# print(group2['Sales'].sum(),group2['Unit'].mean())
# print('-' * 100)
# group3 = sales.groupby(by='Product')
# print(group3.sum('Sales'))