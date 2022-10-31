def round_floats(x):
  if x.dtype == np.float64:
    return round(x)

  return x


# applies the above function to all features in df
players.apply(round_floats)

players.select_dtypes(np.float64).head()

# apply can do aggregations and transformations
data.apply('mean')
data.apply('mean', axis=1)