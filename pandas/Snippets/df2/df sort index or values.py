players.sort_values(by='market_value', ascending=False)

# set index to a field to be sorted

players.set_index('name', inplace=True)

# sort on the new index

players.sort_index(inplace=True)

# sort columns

players.sort_index(axis=1)