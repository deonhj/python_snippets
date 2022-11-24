z_scores = (data - data.mean())/data.std()
data[data.idxmax()]