# M1
players.drop(labels=19, axis=0)
# M2
players.drop(index=[19, 20, 21, 231, 10])


players.drop(index=[2, 10, 21], columns='market_value')