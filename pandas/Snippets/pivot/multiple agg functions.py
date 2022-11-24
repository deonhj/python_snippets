sat.pivot_table('Score', 'Borough', 'SAT Section', aggfunc='max')
sat.pivot_table('Score', 'Borough', 'SAT Section', aggfunc=[np.min, np.max])

sat.pivot_table('Score', 'Borough', 'SAT Section', aggfunc='max')
sat.pivot_table('Score', 'Borough', 'SAT Section', aggfunc=[np.min, np.max])


sat_url = 'https://andybek.com/pandas-sat'
sat = pd.read_csv(sat_url)
sat['Percent Tested'] = sat['Percent Tested'].replace(regex='%', value='').astype(float)

sat.pivot_table(values='Score', index='Borough', columns='SAT Section', aggfunc=['min', 'max'])\
.rename(axis=1, level=0, mapper={'amin':'Minmumu', 'amax':'Maximum'})