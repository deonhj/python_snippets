import pandas as pd
import numpy as np

tech_url = 'https://andybek.com/pandas-tech'
tech = pd.read_csv(tech_url, index_col=['date', 'name'])

# select a list of dates and a list of stocks, and all columns. 
# Note the list of stocks and list of dates are enclosed in a touple
tech.loc[(['2015-01-06', '2015-01-07'], ['FB', 'AMZN']), :]
# selecting only a list of columns
tech.loc[(['2014-01-02', '2014-01-03'], ['AAPL', 'MSFT', 'AMZN']), ['close', 'volume']]

tech.loc[(['2014-01-02', '2014-01-03'], ['AAPL', 'MSFT', 'AMZN']), 'open': 'low']

# slicing does not work as expected. slice is needed
# slice object is used to slice a milti index dataframe
tech.loc[(slice('2014-01-02', '2014-03-03'), ['GOOGL', 'MSFT']), 'open': 'low']
# select all dates 
tech.loc[(slice(None), ['FB', 'AMZN']), 'open']