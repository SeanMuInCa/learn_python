import pandas as pd
import numpy as np
from pandas import Series, DataFrame

series_obj = Series(np.arange(8), index=['row 1', 'row 2', 'row 3', 'row 4', 'row 5', 'row 6','row 7', 'row 8'])
print(series_obj)
print(series_obj['row 7'])
print(series_obj[[1,3]])
arr = pd.Series(data=[7,2,3,4,5])
print(arr)

print('-' * 30)
np.random.seed(25)
DF_obj = DataFrame(np.random.rand(36).reshape((6,6)),
                   index=['row 1', 'row 2', 'row 3', 'row 4','row 5','row 6'],
                   columns=['column 1','column 2','column 3','column 4','column 5','column 6'])
print(DF_obj)

print(DF_obj.loc[['row 2', 'row 5'], ['column 5', 'column 2']])
print('-' * 30)

print(series_obj['row 3':'row 6'])
print('-' * 30)
print(DF_obj < .2)
print('-' * 30)
print(series_obj[series_obj > 6])
print('-' * 30)

# Class Exercise:
# 1) create DF1 having 8*8 size and values varing from 1 to 10
# 2) replace the values more than 7 with 10. display it at the end
np.random.seed(25)
DF_obj2 = DataFrame(np.random.randint(1,11,size=64).reshape((8,8)),
                    index=['row 1', 'row 2', 'row 3', 'row 4','row 5','row 6','row 7','row 8'],
                   columns=['col 1','col 2','col 3','col 4','col 5','col 6', 'col 7','col 8'])
print(DF_obj2)
print('-' * 30)
print(DF_obj2[DF_obj2 > 7]) #????
print('-' * 30)
for i in range(8):
    for j in range(8):
        if DF_obj2.iloc[i,j] > 7:
            DF_obj2.iloc[i,j] = 10
print(DF_obj2)