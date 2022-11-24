sat_url = 'https://andybek.com/pandas-sat'
sat = pd.read_csv(sat_url)
sat['Percent Tested'] = sat['Percent Tested'].replace(regex='%', value='').astype(float)

sat.set_index(['School Name', 'SAT Section']).loc[:, ['Score']].unstack(level=1)

sat.pivot(index='School Name', columns=['SAT Section', 'Borough'], values='Score')
