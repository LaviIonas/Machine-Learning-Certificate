import pandas as pd
import seaborn as sns
import skillsnetwork

import matplotlib.pylab as plt
import numpy as np

sns.set()

def load_data():
    df = pd.read_csv('../data/Ames_Housing_Data.tsv', sep='\t')

    # This is recommended by the data set author to remove a few outliers

    df = df.loc[df['Gr Liv Area'] <= 4000,:]
    print("Number of rows in the data:", df.shape[0])
    print("Number of columns in the data:", df.shape[1])
    data = df.copy() # Keep a copy our original data 

    return data, df

def one_hot(df):
    one_hot_encoded_cols = df.dtypes[df.dtypes == object]
    one_hot_encoded_cols = one_hot_encoded_cols.index.tolist()
    # print(df[one_hot_encoded_cols].head().T)
    df = pd.get_dummies(df, columns=one_hot_encoded_cols, drop_first=True)
    # print(df.head())

def log_transform(data, df):
    mask = data.dtypes == float
    float_cols = data.columns[mask]

    # print(float_cols)

    skew_limit = 0.75
    skew_vals = data[float_cols].skew()

    skew_cols = (skew_vals
                .sort_values(ascending=False)
                .to_frame()
                .rename(columns={0:'skew'})
                .query('abs(skew) > {}'.format(skew_limit))
                )

    # print(skew_cols) 

    # Choose a field
    field = "BsmtFin SF 1"

    # Create two "subplots" and a "figure" using matplotlib
    fig, (ax_before, ax_after) = plt.subplots(1, 2, figsize=(10, 5))

    # Create a histogram on the "ax_before" subplot
    df[field].hist(ax=ax_before)

    # Apply a log transformation (numpy syntax) to this column
    df[field].apply(np.log1p).hist(ax=ax_after)

    # Formatting of titles etc. for each subplot
    ax_before.set(title='before np.log1p', ylabel='frequency', xlabel='value')
    ax_after.set(title='after np.log1p', ylabel='frequency', xlabel='value')
    fig.suptitle('Field "{}"'.format(field));


if __name__ == "__main__":

    data, df = load_data()
    # print(df.head())
    # print(df.columns.tolist())
    
    one_hot(df)

    log_transform(data, df)
    