pd.merge(ivies4, regions2, right_index=True, left_index=True)

# join is equivalent to the merge above. 
# join is just a simplified version of merge
ivies4.join(regions2)

# can also specify on=
ivies.join(regions2, on='School Name')