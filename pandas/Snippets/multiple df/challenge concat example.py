import pandas as pd
import numpy as np

# DATA URL SOURCES ###############################
eng_url     = 'https://andybek.com/pandas-eng'
state_url   = 'https://andybek.com/pandas-state'
party_url   = 'https://andybek.com/pandas-party'
liberal_url = 'https://andybek.com/pandas-liberal'
ivies_url   = 'https://andybek.com/pandas-ivies'
##################################################

eng = pd.read_csv(eng_url)
state = pd.read_csv(state_url)
party = pd.read_csv(party_url)
liberal = pd.read_csv(liberal_url)
ivies = pd.read_csv(ivies_url)

dfs = [state, eng, liberal, ivies, party]

schools = pd.concat(dfs).drop_duplicates(subset='School Name')

schools.reset_index(drop=True, inplace=True)

liberal_test = liberal.copy()
state_test = state.copy()
liberal_test['Mid-Career Median Salary'] = liberal_test.loc[:, 'Mid-Career Median Salary'].replace(r'\$|,', '', regex=True).astype('float')
state_test['Mid-Career Median Salary'] = state_test.loc[:, 'Mid-Career Median Salary'].replace(r'\$|,', '', regex=True).astype('float')

l = liberal_test.sort_values(by='Mid-Career Median Salary', ascending=False).iloc[:3, [0, 3]]  # [From Row 0:To Row 3, [Column 0, Column 3]]
s = state_test.sort_values(by='Mid-Career Median Salary', ascending=False).iloc[:3, [0, 3]]  # [From Row 0:To Row 3, [Column 0, Column 3]]

pd.concat([l, s], axis=1, keys=['Liberal Arts', 'State'])

print('Done')