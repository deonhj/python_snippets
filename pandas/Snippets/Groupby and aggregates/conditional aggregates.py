import pandas as pd
import numpy as np

games_url = 'https://andybek.com/pandas-games'
games = pd.read_csv(games_url)

sales =  games.loc[:, ['Platform', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']]

sales.sum(numeric_only=True)

sales.loc[games.Platform == 'X360'].sum(numeric_only=True)

games.loc[:, ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Global_Sales']].sum()

sales.loc[games.Platform == 'PS3'].sum(numeric_only=True)