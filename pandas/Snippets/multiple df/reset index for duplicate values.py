schools.reset_index(drop=True, inplace=True)

# Alternatively do this when loading the data

pd.concat(dfs, ignore_index=True).drop_duplicates(subset=['School Name']).index.duplicated().sum()