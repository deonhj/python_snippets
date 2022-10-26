from string import ascii_uppercase
labeled_values = pd.Series(list(ascii_uppercase), map(lambda x: '<-' + x + '->', list(ascii_uppercase)))
labeled_values