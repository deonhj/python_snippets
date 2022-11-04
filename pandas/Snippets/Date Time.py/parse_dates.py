import pandas as pd
import numpy as np

oil_url = 'https://andybek.com/pandas-oil'
brent = pd.read_csv(oil_url, index_col='Date', parse_dates=True)


import pandas as pd
import numpy as np

oil_url = 'https://andybek.com/pandas-oil'
brent = pd.read_csv(oil_url, index_col=0, parse_dates=True)