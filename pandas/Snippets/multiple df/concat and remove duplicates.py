pd.concat(dfs)[pd.concat(dfs).duplicated(subset=['School Name'], keep='first')]