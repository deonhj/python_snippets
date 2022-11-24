import pandas as pd
import numpy as np

games_url = 'https://andybek.com/pandas-games'
games = pd.read_csv(games_url)

sales =  games.loc[:, ['Platform', 'Genre', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']]

ser = games.loc[:, ['Genre', 'Global_Sales']].set_index('Genre').squeeze()

ser.groupby('Genre').mean().sort_values(ascending=False)