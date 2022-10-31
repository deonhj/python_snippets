# row order: 2, 1, 3, 0
# column order: age, name, position, club
players_lite.reindex(index=[2,1,3,0], columns=['age', 'name', 'position', 'club'])


# sorted columns
#M1
players.reindex(index=[2,1,3,0]).sort_index(axis=1)
#M2
players.reindex(index=[2,1,3,0], columns=sorted(players.columns)[:6]) # [:6] first 6 items in players.columns

#M3
players.reindex(index=[2,1,3,0], columns=players.columns.sort_values())