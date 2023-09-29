import skillsnetwork
import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pylab as plt

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler

from scipy.stats import norm
from scipy import stats

path = "../data/Ames_Housing_Data1.tsv"
housing = pd.read_csv(path, sep='\t')

# print(housing.head(10))
# print(housing.info())
# print(housing['SalePrice'].describe())
# print(housing['Sale Condition'].value_counts())


hous_num = housing.select_dtypes(include = ['float64', 'int64'])
hous_num_corr = hous_num.corr()['SalePrice'][:-1] # -1 means that the latest row is SalePrice
top_features = hous_num_corr[abs(hous_num_corr) > 0.5].sort_values(ascending=False) #displays pearsons correlation coefficient greater than 0.5
# print("There is {} strongly correlated values with SalePrice:\n{}".format(len(top_features), top_features))

# for i in range(0, len(hous_num.columns), 5):
#     sns.pairplot(data=hous_num,
#                 x_vars=hous_num.columns[i:i+5],
#                 y_vars=['SalePrice'])

# sp_untransformed = sns.distplot(housing['SalePrice']).show()

# print("Skewness: %f" % housing['SalePrice'].skew())
#
# log_transformed = np.log(housing['SalePrice'])
# sp_transformed = sns.distplot(log_transformed)
# print("Skewness: %f" % (log_transformed).skew())

# la_plot = sns.distplot(housing['Lot Area'])
# print("Skewness: %f" % housing['Lot Area'].skew())
#
# la_log = np.log(housing['Lot Area'])
# print("Skewness: %f" % la_log.skew())

# duplicate = housing[housing.duplicated(['PID'])]
# print(duplicate)
#
# dup_removed = housing.drop_duplicates()
# print(dup_removed)

# print(housing.index.is_unique)
#
# mean = housing["Mas Vnr Area"].mean()
# housing['Mas Vnr Area'].fillna(mean, inplace=True)
