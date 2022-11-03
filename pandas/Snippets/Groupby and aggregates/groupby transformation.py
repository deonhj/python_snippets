import pandas as pd
import numpy as np

games_url = 'https://andybek.com/pandas-games'
games = pd.read_csv(games_url)

games_relative = games.loc[:, ['Name', 'Genre', 'Platform', 'Global_Sales']]
# convert raw global_sales to within-genre standard scores
games_relative.set_index(['Name', 'Platform']).groupby('Genre').transform(lambda x: (x - x.mean())/x.std())\
      .sort_values(by='Global_Sales', ascending=False)



game_sale      = 5
game_genre_avg = 5.05
game_genre_std = 0.1
(game_sale - game_genre_avg) / game_genre_std