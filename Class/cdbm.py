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
print('-'*100)
import kagglehub

# Download latest version
path = kagglehub.dataset_download("gunjanpathak/melb-data")

print("Path to dataset files:", path)

newFile = pd.read_csv(path+'\melb_data.csv')
print(newFile.info())
print(newFile.isnull().sum())
d1 = newFile.ffill()
print(d1.info())
d2 = d1.bfill()
print(d2.info())
print(d2.isnull().sum())
print('-'*100)
data = { 'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', None], 'Age': [24, None, 22, 23, None, 29], 'Score': [85, 70, None, 88, 95, 90], 'City': ['New York',
'Los Angeles', None, 'Chicago', 'Houston', None] }
df = pd.DataFrame(data)
print(df.isnull())
print('-'*100)
d1= df.dropna()
print(d1)
print('-'*100)
d2 = df.dropna(axis=1)
print(d2)
print('-'*100)
d3 = df.dropna(axis=1, thresh=len(data.keys()))
print(d3)
print('-'*100)
d4 = df[df.isnull().sum(axis=1) != len(data.keys())]
print(d4)
print('-'*100)
d5 = df.dropna(how='any')
print(d5)
print('-'*100)
d6 = df.dropna(how='all')
print(d6)
print('-'*100)
d7 = df.fillna(0)
print(d7)
print('-'*100)
d8 = df.ffill()
print(d8)
print('-'*100)
d9 = df.bfill()
print(d9)
d10 = df[df.isnull()]
print(d10)