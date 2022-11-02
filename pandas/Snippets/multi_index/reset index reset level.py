tech.reset_index()
tech.reset_index(level=['volume_type', 'name'], drop=True)
tech.droplevel(['volume_type', 'name'])
tech.droplevel([1, 2])