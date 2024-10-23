import numpy as np
import pandas as pd
from pandas import Series, DataFrame

obj = DataFrame({'column 1': [1,1,2,2,3,3,3,],
                 'column 2': ['a','a','b','b','c','c','c'],
                 'column 3': ['A','A','B','B','C','C','C']})
print(obj)
print('-'*100)
print(obj.duplicated())
print('-'*100)
df2 = obj.drop_duplicates()
print(df2)
print(obj)
print('-'*100)
obj1 = DataFrame({'column 1': [1,1,2,2,3,3,3,],
                 'column 2': ['a','a','b','b','c','c','c'],
                 'column 3': ['A','A','B','B','C','D','C']})
print(obj1.duplicated())
print(obj1.drop_duplicates())
print('-'*100)
df3 = obj1.drop_duplicates(['column 3']) # keep only the first row of each group based on the column 3
print(df3)
