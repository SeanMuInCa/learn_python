# # Class exercise 1:
# 1. Create a Pandas Series of 5 fruit names:
# ["Apple", "Banana", "Mango", "Grapes", "Orange"]
#
# 2. Access the following elements:
# The first element.
# The last element.
# The element at index 2.
#
# 3. Slice the Series to get:
# The first 3 elements.
# All elements except the first one.
#
# 4. Check if "Mango" is present in the Series.

import pandas as pd
from pandas import Series, DataFrame
fruits = Series(["Apple", "Banana", "Mango", "Grapes", "Orange"])
print(fruits[0])
print(fruits[4])
print(fruits[2])
print(fruits[0:3])
print(fruits[1:])
print("Mango" in fruits)

# Class exercise 2:
# 1. Create a DataFrame using the following dictionary:
#
# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
#     'Age': [24, 27, 22, 32, 29],
#     'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
# }
#
# 2. Access elements and rows:
#
# Get the first row of the DataFrame.
#
# Access the 'Age' column.
#
# Get the age of the person at index 3.
#
# 3. Slice the DataFrame:
#
# Get the first 3 rows.
#
# Get the 'Name' and 'City' columns for the last 2 rows.
#
# 4. Filter rows:
# Get all rows where Age > 25.
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [24, 27, 22, 32, 29],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}
print('-' * 100)
dataFrame = DataFrame(data)
print(dataFrame.iloc[0])
print(dataFrame['Age'])
print(dataFrame['Age'][3])
print(dataFrame.iloc[0:3])
print(dataFrame.iloc[-2:, [0, 2]])
print(dataFrame[dataFrame['Age'] > 25])