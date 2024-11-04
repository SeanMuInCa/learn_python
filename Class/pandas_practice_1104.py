import pandas as pd

movies = pd.read_csv('d:\\mysask\\AI\\ml-32m\\movies.csv', sep=',')
print(movies.head(15))
print(type(movies))
print('-' * 100)
tags = pd.read_csv('d:\\mysask\\AI\\ml-32m\\tags.csv', sep=',')
print(tags.head())
print('-' * 100)
#
# rating = pd.read_csv('d:\\mysask\\AI\\ml-32m\\ratings.csv', sep=',', parse_dates=['timestamp'])
rating = pd.read_csv('d:\\mysask\\AI\\ml-32m\\ratings.csv', sep=',')
# rating['timestamp'] = pd.to_numeric(rating['timestamp'], errors='coerce')  # 强制转换为数值类型
# rating['timestamp'] = pd.to_datetime(rating['timestamp'], unit='s')
# print(rating.head())

row_0 = tags.iloc[0]

print(row_0)
print(row_0.index)
print(row_0['userId'])
print('tag' in row_0)
print(row_0.name)
row_0 = row_0.rename('darshan sucks')
print(row_0.name)
print('-' * 100)
print(tags.describe())
print(tags.mode())
# print(rating.corr())
print('-' * 100)
comedy = movies['genres'].str.contains('Comedy')
print(comedy.head())
print('-' * 100)
print(rating[['movieId', 'rating']].groupby('rating').count())