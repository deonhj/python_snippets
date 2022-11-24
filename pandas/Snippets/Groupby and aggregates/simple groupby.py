# The group by just creates the grouping it does not apply an aggregation

import pandas as pd
import numpy as np

games_url = 'https://andybek.com/pandas-games'
games = pd.read_csv(games_url)

sales =  games.loc[:, ['Platform', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']]

sales.groupby('Platform').sum()
sales.groupby('Platform').median()
sales.groupby('Platform').mean()

import pandas as pd
import numpy as np

games_url = 'https://andybek.com/pandas-games'
games = pd.read_csv(games_url)

sales =  games.loc[:, ['Platform', 'Genre', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']]

sales.groupby(['Platform', 'Genre']).sum()


import pandas as pd
import numpy as np

games_url = 'https://andybek.com/pandas-games'
games = pd.read_csv(games_url)

studios = games.loc[:, ['Genre', 'Publisher', 'Global_Sales']]

studios.groupby('Publisher').sum(numeric_only=True).sort_values(by='Global_Sales', ascending=False)

games.groupby('Year').sum()['Global_Sales'].nlargest(3)