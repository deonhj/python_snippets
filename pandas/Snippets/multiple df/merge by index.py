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

ivies4 = ivies.set_index('School Name')
regions2 = regions.set_index('School Name')

# Merging by index
pd.merge(ivies4, regions2, left_index=True, right_index=True)

# Merge on a combination of index and column
pd.merge(ivies4, regions, left_index=True, right_on='School Name')