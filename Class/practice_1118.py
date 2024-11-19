import pandas as pd
import numpy as np

arr = np.array([1,2,3,4])
print(arr, type(arr),arr.ndim)
print(arr.shape)


arr1 = np.array([[1,2,3],[4,5,6]])
print(arr1.ndim)

arr2 = arr * 3
print(arr)
print(arr2)
print(arr + arr2)
print(arr.ndim)
arr3 = np.array([1,'233',{1}])
print(arr3)
print(arr3.dtype)