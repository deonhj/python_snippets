import pandas as pd
import numpy as np

tech_url = 'https://andybek.com/pandas-tech'
tech = pd.read_csv(tech_url, index_col=['date', 'name'])
tech
# example 1
tech.loc[('2014-01-02', 'GOOGL'), 'close']
# example 2
tech.loc[('2019-08-23', 'MSFT'), 'open':'close']
# iloc ignores the indexes completely
tech.iloc[2,4]