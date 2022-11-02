import pandas as pd
import numpy as np

games_url = 'https://andybek.com/pandas-games'
games = pd.read_csv(games_url)

sales = games.loc[:, ['Platform', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']]

for i, j in sales.groupby('Platform'):
    print(i)
    print(j)