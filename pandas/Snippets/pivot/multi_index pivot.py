sat.pivot_table(values='Score', columns=['School Name', 'Borough'], index='SAT Section')


sat.loc[sat.Borough == 'Queens'][['SAT Section', 'Score', 'School Name']]\
.pivot_table(index ='School Name', columns='SAT Section', values='Score').sort_values(by='Math', ascending=False)