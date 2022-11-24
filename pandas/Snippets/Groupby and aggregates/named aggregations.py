import pandas as pd
import numpy as np

games_url = 'https://andybek.com/pandas-games'
games = pd.read_csv(games_url)

studios = games.loc[:, ['Genre', 'Publisher', 'Global_Sales']]

studios.groupby('Publisher')['Global_Sales'].agg(['sum', 'max', 'min', 'count']).sort_values('sum', ascending=False)

studios.groupby(['Genre', 'Publisher']).agg(['sum', 'count', 'mean', 'std'])\
       .rename({'sum': 'total_revenue', 'count': 'num_games'}, axis=1)

studios.groupby(['Genre', 'Publisher']).agg(
    total_revenue=('Global_Sales','sum'), 
    num_games=('Global_Sales', np.mean),
    revenue_std=('Global_Sales', 'std'),
    revenue_avg=('Global_Sales', 'mean')
    ).sort_values(by='total_revenue', ascending=False)

# Notice that the method below is referencing different columns

games.groupby(['Genre', 'Publisher']).agg(
    total_global_revenue=('Global_Sales', 'sum'),
    average_EU_revenue=('EU_Sales', 'mean')
)