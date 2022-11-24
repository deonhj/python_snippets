data.select_dtypes(np.number).agg(np.min)

data.select_dtypes(np.number).agg('max')

players.select_dtypes(np.number).agg(['min', 'max', 'mean'])