import pandas as pd
import numpy as np

games_url = 'https://andybek.com/pandas-games'
games = pd.read_csv(games_url)

studios = games.loc[:, ['Genre', 'Publisher', 'Global_Sales']]

studios.groupby(['Genre', 'Publisher']).sum(numeric_only=True).sort_index().sort_values(by=['Genre','Global_Sales'], ascending=[False, False])