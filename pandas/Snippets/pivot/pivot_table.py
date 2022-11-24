sat_url = 'https://andybek.com/pandas-sat'
sat = pd.read_csv(sat_url)
sat['Percent Tested'] = sat['Percent Tested'].replace(regex='%', value='').astype(float)

sat.pivot_table(values='Score', index='Borough', columns='SAT Section')

sat.pivot_table(values='Score', index='Borough', columns='SAT Section', aggfunc='std')

sat.pivot_table(values='Percent Tested', index='Borough')

sat.pivot_table(values='Percent Tested', index='Borough', aggfunc='min')