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

# Display the first few rows of the cleaned DataFrame
print(gameSalesCleaned.head())
