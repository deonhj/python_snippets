import pandas as pd
import numpy as np

games_url = 'https://andybek.com/pandas-games'
games = pd.read_csv(games_url)

ps3 = games.loc[games.Platform == 'PS3', ['Name', 'Genre', 'EU_Sales', 'Global_Sales']]
# the paradigm: subgroup -> apply() -> output
ps3.groupby('Genre').apply(lambda sg: 'solid' if sg.EU_Sales.sum() > 50 else 'weak')

def sales_detail(sg):
    level = 'solid' if sg.EU_Sales.sum() > 50 else 'weak'
    variability = 'volatile' if sg.EU_Sales.std()/sg.EU_Sales.mean() > 2 else 'steady'
    return (variability, level + ' sales')


ps3.groupby('Genre').apply(sales_detail)

ps3.groupby('Genre').apply(lambda x: print(x.info(), '\n'))