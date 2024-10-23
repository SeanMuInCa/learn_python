import pandas as pd

import numpy as np
missing = np.nan
np.random.seed(25)
obj = pd.DataFrame(np.random.randn(36).reshape(6,6))
print(obj)

obj.loc[3:5, 0] = missing
obj.loc[1:4, 5] = missing
print(obj)

print(obj.isnull())

filled_obj=obj.fillna(0) # not going to change obj
print(filled_obj)

f2 = obj.fillna({0:0.1, 5:1.2})
print(f2)
print('-'*100)
f3=obj.ffill() #from top to bottom
print(f3)
print('-'*100)
f4=obj.bfill() #from bottom to top
print(f4)
print(obj.info()) # check basic information of the obj
print('-'*100)
print(obj.isnull().sum()) # by column

print('-'*100)
f5=obj.dropna() # if there is any missing value, drop the whole row
print(f5)

print('-'*100)
f6=obj.dropna(axis=1) # drop the whole column if there is any missing value
print(f6)