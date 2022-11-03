import pandas as pd
import numpy as np

games_url = 'https://andybek.com/pandas-games'
games = pd.read_csv(games_url)

games.groupby(['Publisher', 'Genre']).filter(lambda sg: sg['NA_Sales'].sum() > 50)

# Another Example

def more_than_50(df):
    return df['NA_Sales'].sum() > 50

 games.groupby(['Publisher', 'Genre']).filter(more_than_50) 



# pective Platform sold more in Japan (JP_Sales) than in Europe (EU_Sales).
 games.groupby(['Platform', 'Genre']).filter(lambda x: x['JP_Sales'].sum() > x.NA_Sales.sum())