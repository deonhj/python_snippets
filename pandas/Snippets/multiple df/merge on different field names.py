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
schools

income_url = 'https://andybek.com/pandas-mid'
mid_career = pd.read_csv(income_url)
mid_career.head()

pd.merge(schools, mid_career, left_on='School Name', right_on='school_name').drop('school_name', axis=1)