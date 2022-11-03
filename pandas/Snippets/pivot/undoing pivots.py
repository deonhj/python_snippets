sat_url = 'https://andybek.com/pandas-sat'
sat = pd.read_csv(sat_url)
sat['Percent Tested'] = sat['Percent Tested'].replace(regex='%', value='').astype(float)

pivoted = sat.pivot(index='School Name', columns='SAT Section', values='Score')

pivoted.stack().reset_index()

pivoted.reset_index().melt(id_vars='School Name', value_name='Score')