import pandas as pd
import numpy as np

oil_url = 'https://andybek.com/pandas-oil'
brent = pd.read_csv(oil_url, index_col='Date', parse_dates=True)

brent.loc['2017-01-03']

brent.loc['2017-01-03':'2017-01-06']

brent.loc['2019-01-02':'2019-01-31']

brent.loc['2019-01'] # partial string indexing

brent.loc['2019-01':'2019-02']

brent['2019-07':'2019-08-15']