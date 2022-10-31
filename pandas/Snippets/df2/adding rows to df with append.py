cristiano = pd.Series({
    'nicknames': 'Cristiano',
    'age': 32,
    'position': 'RW',
    'club': 'Juventus',
    'position_cat': 1
}, name=4)

df_mini = df_mini.append(cristiano)

# Another Example

other_players = pd.DataFrame({
    'nicknames': ['Gianluigi', 'Lionel'],
    'age': [37, 32],
    'club': ['Juventus', 'Barcelona'],
    'position': ['GK', 'CF'],
    'position_cat': [4,2]
}, index=[5,6])

df_mini = df_mini.append(other_players)