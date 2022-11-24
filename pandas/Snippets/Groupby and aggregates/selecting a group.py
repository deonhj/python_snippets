import pandas as pd
import numpy as np

games_url = 'https://andybek.com/pandas-games'
games = pd.read_csv(games_url)

sales = games.loc[:, ['Platform', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']]

# Select a group
sales.groupby('Platform').get_group('PS3')
# Select a group and a field
sales.groupby('Platform').get_group('PS3')['JP_Sales']