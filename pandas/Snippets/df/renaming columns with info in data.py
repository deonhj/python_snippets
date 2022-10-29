import pandas as pd
import numpy as np

dataurl = 'https://andybek.com/pandas-nutrition'
nutrition = pd.read_csv(dataurl, index_col=[0])

nutrition.set_index('name', drop=True, inplace=True)

units_df = nutrition.astype(str).replace('[^a-zA-Z]', '', regex=True)

units = units_df.mode()

units = units.replace('', np.nan).dropna(axis=1)

mapper = {k: k + "_" + units[k].at[0] for k in units}
mapper

nutrition.rename(columns=mapper, inplace=True)

nutrition.head()