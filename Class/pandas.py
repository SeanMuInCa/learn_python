import pandas as pd
import numpy as np
from pandas import Series, DataFrame

series_obj = Series(np.arange(8), index=['row 1', 'row 2', 'row 3', 'row 4', 'row 5', 'row 6','row 7', 'row 8'])
print(series_obj)
print(series_obj['row 7'])

arr = pd.Series(data=[7,2,3,4,5])
print(arr)

print('-' * 30)

DF_obj = DataFrame(np.random.rand(36).reshape((6,6)),
                   index=['row 1', 'row 2', 'row 3', 'row 4','row 5','row 6'],
                   columns=['column 1','column 2','column 3','column 4','column 5','column 6'])
print(DF_obj)