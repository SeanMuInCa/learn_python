import pandas as pd
from pandas import Series, DataFrame
my_series = Series([
4.6, 2.1, -4.0, 3.0],['a','b','c','d'])

print(my_series)
print('-'*100)
df1 = DataFrame()
print(df1)
print('-'*100)
df1 = DataFrame(columns=('Col 1', 'Col 2', 'Col3'))
print(df1)
print('-'*100)
df1 = DataFrame([[1,2,3],[3,4,5]],columns=list(('Col 1', 'Col 2', 'Col3')))
print(df1.shape)

a = DataFrame([[1,2,3],[3,4,5]], columns=list('ABC'))
b = DataFrame([[5,2,3],[7,4,5]], columns=list('BDE'))
c = DataFrame([[11,12,13],[17,14,15]], columns=list('XYZ'))

print(a)
print(b)
print(c)
