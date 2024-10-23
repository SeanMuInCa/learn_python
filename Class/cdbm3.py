import numpy as np
import pandas as pd
from pandas import Series, DataFrame

obj = DataFrame(np.arange(36).reshape(6,6))
print(obj)
print('-'*100)
obj2 = DataFrame(np.arange(15).reshape(5,3))
print(obj2)
print('-'*100)
obj3 = pd.concat([obj,obj2], axis=1)#merge two dataframe, insert by col
print(obj3)
print('-'*100)
obj4 = pd.concat([obj,obj2], axis=0)# merge two dataframe, insert by row, like append
print(obj4)
print('-'*100)
obj5 = obj.drop([0,2])# delete row0and2, because drop works by label not index
print(obj)
print(obj5)