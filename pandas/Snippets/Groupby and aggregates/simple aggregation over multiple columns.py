import pandas as pd
import numpy as np

games_url = 'https://andybek.com/pandas-games'
games = pd.read_csv(games_url)

games.loc[:, ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Global_Sales']].sum()
games.loc[:, ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']].max(axis=1)