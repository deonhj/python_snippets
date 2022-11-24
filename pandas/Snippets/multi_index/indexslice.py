tech.loc[pd.IndexSlice[:, ['FB', 'AMZN']], 'high':'low']

i = pd.IndexSlice

tech.loc[i[:, 'FB'], 'high':'low']

# Firther Example
iimport pandas as pd
import numpy as np

tech_url = 'https://andybek.com/pandas-tech'
tech = pd.read_csv(tech_url, index_col=['date', 'name'])
tech.head()

tech.set_index('volume_type', append=True, inplace=True)
tech

idx = pd.IndexSlice
tech.loc[idx[:, ['FB', 'AMZN'], 'medium'], ['low', 'high', 'volume']]


idx = pd.IndexSlice
tech_df3.loc[idx[2019, 1:3, :], ['low', 'high', 'volume']]

# Web example
idx = pd.IndexSlice

dfmi.loc[idx[:, :, ["C1", "C3"]], idx[:, "foo"]]