from cProfile import label

import pandas as pd
import numpy as np

# Step 1: Select a real-world dataset
gameSales = pd.read_csv("vgsales.csv")

# Step 2: Perform data preparation & cleaning
print(gameSales.shape)
print('-' * 100)
print(gameSales.describe())
print('-' * 100)
print(gameSales.info())
print('-' * 100)
print(gameSales.isnull().sum())
print('-' * 100)

# Drop rows with missing values
gameSalesCleaned = gameSales.dropna().copy()

# Add a new column '21 Central' based on a condition
gameSalesCleaned['21 Central'] = np.where(gameSalesCleaned['Year'] > 2000, '21st', '20th')
print('-' * 100)
# Step 3: Perform exploratory analysis & visualization
# calculate mean values
GlobalSalesMeanValues = gameSalesCleaned['Global_Sales'].mean()
print(f'The mean value of Global Sales is: {GlobalSalesMeanValues} Millions')
print('-' * 100)
# calculate range values
NorthAmericaSalesRange = gameSalesCleaned['NA_Sales'].max() - gameSalesCleaned['NA_Sales'].min()
print(f'The range of North America Sales is: {NorthAmericaSalesRange} Millions')
print('-' * 100)
# calculate sum values of Japan sales
SumJapanSales = gameSalesCleaned['JP_Sales'].sum()
print(f'The sum of Japan Sales is: {SumJapanSales} Millions')
print('-' * 100)
import matplotlib.pyplot as plt

genres = gameSalesCleaned['Genre'].unique()  # Get unique genres

fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
salsByGenre = gameSalesCleaned.groupby('Genre')['Global_Sales'].sum()
# 12 colors
# ax.bar(genres, salsByGenre,color=['skyblue', 'yellowgreen', 'lightpink', '#f40', '#f90', 'lightblue', 'lightcoral', 'lightgreen', 'lightyellow', 'lightgray', 'lightseagreen', 'yellow'],label=genres)
ax.hist(salsByGenre, bins=12)
ax.set_xticklabels([])
plt.xlabel('Genre')
plt.ylabel('Global Sales (in millions)')
plt.title('Global Sales by Genre')
plt.legend()
# # Create a histogram for each genre
# for genre in genres:
#     # Filter data for the current genre
#     genre_data = gameSalesCleaned[gameSalesCleaned['Genre'] == genre]
#
#     # Plot histogram for NA_Sales
#     plt.hist(genre_data['NA_Sales'], bins=20, label=genre)
#
# # Adding labels and title
# plt.title('NA Sales Distribution by Genre')
# plt.xlabel('NA Sales (in millions)')
# plt.ylabel('Frequency')
# plt.legend()

# Show the plot
plt.show()



