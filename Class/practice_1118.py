import pandas as pd
import numpy as np

arr = np.array([1,2,3,4])
print(arr, type(arr),arr.ndim)
print(arr.shape)
arr.shape = (2,2)
print(arr)
print(arr, type(arr),arr.ndim)

arr1 = np.array([[1,2,3],[4,5,6]])
print(arr1.ndim)
