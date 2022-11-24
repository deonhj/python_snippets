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

stacked = tech.stack()
names = stacked.index.names
stacked.index.set_names([*names[:-1], 'Previously a Column Axis'], inplace=True)

stacked.unstack(level='Trading Date')