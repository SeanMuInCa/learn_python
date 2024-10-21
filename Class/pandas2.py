import pandas as pd

my_series = pd.Series([
4.6, 2.1, -4.0, 3.0])

print(my_series)
df1 = pd.DataFrame()
print(df1)
df1 = pd.DataFrame(columns=('Col 1', 'Col 2', 'Col3'))
print(df1)
df1 = pd.DataFrame([[1,2,3],[3,4,5]],columns=list(('Col 1', 'Col 2', 'Col3')))
print(df1.shape)

a = pd.DataFrame([[1,2,3],[3,4,5]], columns=list('ABC'))
b = pd.DataFrame([[5,2,3],[7,4,5]], columns=list('BDE'))
c = pd.DataFrame([[11,12,13],[17,14,15]], columns=list('XYZ'))

print(a)
print(b)
print(c)
