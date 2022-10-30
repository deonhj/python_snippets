players[players.duplicated()]

players.loc[players.duplicated(subset=['club', 'age', 'position', 'market_value'])]

players.loc[players.duplicated(subset=['club', 'age', 'position', 'market_value'], keep='last')]

# removing duplicates

players.drop_duplicates(keep='first').market_value.mean()


players.drop_duplicates(subset=['age', 'club', 'position'], keep='first').drop(columns='club')