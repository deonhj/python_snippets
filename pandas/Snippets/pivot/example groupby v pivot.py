sat_url = 'https://andybek.com/pandas-sat'
sat = pd.read_csv(sat_url)
sat['Percent Tested'] = sat['Percent Tested'].replace(regex='%', value='').astype(float)

# Both below lines achieve the same result
sat.pivot_table('Score','Borough','SAT Section')
sat.groupby(['Borough', 'SAT Section']).agg({'Score':'mean'}).unstack()