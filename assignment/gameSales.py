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
