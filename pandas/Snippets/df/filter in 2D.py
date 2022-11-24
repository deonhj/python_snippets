import pandas as pd
import numpy as np

dataurl = 'https://andybek.com/pandas-nutrition'
nutrition = pd.read_csv(dataurl, index_col=[0])

nutrition.set_index('name', drop=True, inplace=True)
nutrition.head()

nutrition.filter(like='corn', axis=0)

nutrition.filter(regex='[Cc]orn', axis=0)

nutrition.filter(regex='[Cc]orn', axis=0)\
         .filter(items=['cholesterol', 'serving_size', 'calories'] ,axis=1)

# OR

nutrition.filter(regex='(?i)octopus', axis=0)\
         .loc[:, ['cholesterol_mg', 'serving_size_g', 'calories']]