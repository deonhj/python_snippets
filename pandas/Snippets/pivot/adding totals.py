sat_url = 'https://andybek.com/pandas-sat'
sat = pd.read_csv(sat_url)
sat['Percent Tested'] = sat['Percent Tested'].replace(regex='%', value='').astype(float)

sat.pivot_table('Score', 'Borough', 'SAT Section', aggfunc='mean', margins=True) 