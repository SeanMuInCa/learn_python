import pandas as pd
import numpy as np
from pandas import Series, DataFrame

cars = pd.read_csv('D:\\mysask\\AI\\mtcars.csv')
cars.columns = ['car_names','mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']
print(cars.head())
print('-' * 100)
print(cars.describe())
print('-' * 100)
cars_group1 = cars.groupby(cars['cyl'])
print(cars_group1.describe()) # describe is powerful tool, check the output