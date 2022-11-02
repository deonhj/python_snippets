import pandas as pd
import numpy as np

games_url = 'https://andybek.com/pandas-games'
games = pd.read_csv(games_url)

sales =  games.loc[:, ['Platform', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']]

sales

platform_names = {
    'PS3': 'PlayStation',
    'PS4': 'PlayStation',
    'X360': 'XBox',
    'XOne': 'XBox'
}
# create a custom grouping mapping for the groupby
sales.set_index('Platform').groupby(platform_names).sum()