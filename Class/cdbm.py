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