chelsea_23under = (players.club == 'Chelsea') & (players.age.le(23))

players.loc[chelsea_23under, ['position', 'market_value']]

# Another example

p_cols = players.columns.str.startswith('p')
players.loc[chelsea_23under, p_cols]