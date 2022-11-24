players[
        (players.position == 'LB') &
        (players.age <= 25) &
        (players.market_value >= 10) &
        ~(players.club.isin(['Tottenham', 'Arsenal']))
        ]


# Or assign each condition to a variable 

players.loc[arsenal_player & right_back | chelsea_and_GK]

# Another example

players[(players.nationality == 'England') & (players.market_value > mv_avg2) & ((players.page_views > 4000) ^ (players.new_signing == 1))]