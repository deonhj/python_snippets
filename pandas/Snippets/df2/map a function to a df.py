players.loc[:, ['market_value', 'fpl_value']].transform(lambda x: x * 0.91)

# Above is the same as below

players.loc[:, ['market_value', 'fpl_value']] * 0.91

# Applyinf a custom function

def random_case(x):
  funcs = [x.str.swapcase, x.str.lower, x.str.title, x.str.upper]

  return choice(funcs)()


(players.select_dtypes(include=object).transform(random_case).head()
