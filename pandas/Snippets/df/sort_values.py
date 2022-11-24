import pandas as pd
import numpy as np

dataurl = 'https://andybek.com/pandas-nutrition'
nutrition = pd.read_csv(dataurl, index_col=[0])

nutrition.set_index('name', drop=True, inplace=True)

nutrition.sort_values(by=['cholesterol', 'sodium'], ascending=[False, True])

nutrition.loc['Beef, simmered, cooked, brain, variety meats and by-products'].filter(like='_g').sort_values(ascending=False)
