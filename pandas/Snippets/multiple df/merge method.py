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

regions_url = 'https://andybek.com/pandas-regions'
regions = pd.read_csv(regions_url)
regions

pd.merge(schools, regions) # merging automatically happens on the common fields.

# Can also be more explicitly states with on keyword

pd.merge(schools, regions, on='School Name')