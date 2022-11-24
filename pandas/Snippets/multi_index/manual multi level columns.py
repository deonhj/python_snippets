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

cols = pd.MultiIndex.from_product([['low', 'high'], ['MSFT', 'AMZN']], names=['Volume Category', 'Ticker'])
cols

low = tech['Volume Category'] == 'low'
high = tech['Volume Category'] == 'high'
amzn = tech.Ticker == 'AMZN'
msft = tech.Ticker == 'MSFT'

data = [
 tech[low & msft].close.sample(10).values,
 tech[low & amzn].close.sample(10).values,
 tech[high & msft].close.sample(10).values,
 tech[high & amzn].close.sample(10).values
]

data = [ [*i] for i in zip(*data)]

df = pd.DataFrame(data, columns=cols)

df