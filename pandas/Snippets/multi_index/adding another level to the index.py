import pandas as pd
import numpy as np

tech_url = 'https://andybek.com/pandas-tech'
tech = pd.read_csv(tech_url, index_col=['date', 'name'])
tech.head()

tech.set_index('volume_type', append=True, inplace=True)
tech

idx = pd.IndexSlice
tech.loc[idx[:, ['FB', 'AMZN'], 'medium'], ['low', 'high', 'volume']]