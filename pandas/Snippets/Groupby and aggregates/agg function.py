import pandas as pd
import numpy as np

games_url = 'https://andybek.com/pandas-games'
games = pd.read_csv(games_url)

studios = games.loc[:, ['Genre', 'Publisher', 'Global_Sales']]

studios.groupby('Publisher')['Global_Sales'].agg(['sum', 'max', 'min', 'count']).sort_values('sum', ascending=False)

