import numpy as np
import pandas as pd


# %%
ex1 = pd.Series([0, np.nan, '', None])
ex1


# %%
ex2 = np.array([2, np.nan, 6, 8])
ex2.sum(), ex2.min(), ex2.max()


# %%
ex1.isnull()


# %%
ex1[ex1.notnull()]


# %%
ex1.dropna()


# %%
ex3 = pd.DataFrame([[1,     np.nan, 7],
                    [2,     5,      8],
                    [np.nan, 6,     9]])
ex3.dropna()


# %%
ex3.fillna(0)


# %%
dup = pd.DataFrame({'letters': ['A','B'] * 2 + ['B'],
                    'numbers': [1, 2, 1, 3, 3]})
dup


# %%
dup.duplicated()


# %%
dup.drop_duplicates()


# %%
dup.drop_duplicates(['letters'])


# %%
sales = pd.read_csv('../Module5/sales_data_sample.csv', encoding='latin')


# %%
data = pd.DataFrame(sales.loc[:50,['ORDERNUMBER', 'QUANTITYORDERED', 'SALES', 'CUSTOMERNAME', 'ADDRESSLINE1', 'POSTALCODE', 'STATUS']])
data


# %%
data.rename(columns={'ORDERNUMBER':'ORDER_ID', 'ADDRESSLINE1':'ADDRESS'}, inplace=True)
data


# %%
data.columns[data.columns != 'STATUS']


# %%
data[data['SALES'] > 5000]


# %%
data[data['CUSTOMERNAME'].str.contains('Ltd')]


# %%
data.loc[(data.SALES > 5000), 'STATUS'] = 'Canceled'
data