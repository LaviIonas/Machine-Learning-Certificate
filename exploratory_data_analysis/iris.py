import os
import numpy as np
import pandas as pd

filepath = "../data/iris_data.csv"
data = pd.read_csv(filepath)
# print(data.head())

# Question 1

# print(data.shape[0])
# print(data.columns.tolist())
# print(data.dtypes)

# Question 2

# data['species'] = data.species.str.replace('Iris-', '')
# data['species'].apply(lambda x: x[5:])
# print(data.head())

# Question 3

# print(data.species.value_counts())
# stats_df = data.describe()
# stats_df.loc['range'] = stats_df.loc['max'] - stats_df.loc['min']
# out_fields = ['mean', '25%', '50%', '75%', 'range']
# stats_df = stats_df.loc[out_fields]
# stats_df.rename({'50%' : 'median'}, inplace=True)
# print(stats_df)

# Question 4
