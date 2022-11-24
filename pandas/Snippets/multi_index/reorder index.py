tech.index.reorder_levels([2, 1, 0])
tech.reorder_levels([2, 0, 1])
tech = tech.swaplevel('volume_type', 'name')
tech.swaplevel(i=2,j=1)