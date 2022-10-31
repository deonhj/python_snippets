# vectorized ops: agg(), transform(), apply()
# above are applied in a vectorised fashoin on each Series in the DF as a whole

# non-vectorized: applymap()
# applymap is applies element by element in a series

mini_df = players.loc[:, ['market_value', 'fpl_value']]


from datetime import datetime
counter = 0

def log_and_transform(x):
  global counter
  counter += 1
  if counter % 100 == 0:
    print(f"It's {datetime.now()} and I just adjusted the {counter}th value.")
    # print("It's {} and I just adjusted the {}th value.".format(datetime.now(), counter))
  
  return x * inflation


mini_df.applymap(log_and_transform)