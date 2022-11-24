import pandas as pd
import numpy as np

boston_url = 'https://andybek.com/pandas-marathon'

boston = pd.read_csv(boston_url)

boston['First Name'] = boston.Name.str.split(', ').str.get(1)
boston['Last Name'] = boston.Name.str.split(', ').str.get(0)

boston.drop(['First Name', 'Last Name'], axis=1, inplace=True)

boston[['First Name', 'Last Name']] = boston.Name.str.split(', ', expand=True)


boston.Name.str[:2]