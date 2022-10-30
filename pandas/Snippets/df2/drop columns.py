players.drop(labels=['age', 'market_value'], axis='columns')

# Alternative
players.drop(columns=['age', 'market_value', 'name'])

# Alternative
players.pop('age')

# Alternative
unwanted_rows = [1,2,3,4]
unwanted_columns = ['name', 'position', 'position_cat']
players.reindex(
    index=set(players.index).difference(unwanted_rows),
    columns=set(players.columns).difference(unwanted_columns)
    )


players.drop(index=[2, 10, 21], columns='market_value')