import pandas as pd
import numpy as np

tech_url = 'https://andybek.com/pandas-tech'
tech = pd.read_csv(tech_url, index_col=['date', 'name'])
tech.head()

tech.set_index('volume_type', append=True, inplace=True)
tech

tech = tech.swaplevel('volume_type', 'name')

tidx=tech.index
tidx.set_names(['Trading Date', 'Volume Category', 'Ticker'], inplace=True)

tech.reset_index(inplace=True)
tech.head()

tech_df3 = tech.set_index(keys=['year', 'month', 'day'])

idx = pd.IndexSlice
tech_series = tech_df3.loc[idx[2019, 1:3, :], :].stack()
tech_series.loc[(slice(None), slice(None), slice(None), 'close')].mean()
tech_series.loc[(slice(None), slice(None), slice(None), 'close')].std()
tech_series.loc[(slice(None), slice(None), slice(None), 'close')].apply({'Average Price': 'mean', 'Standard Deviation of Price': 'std'})