from string import ascii_uppercase
labeled_values = pd.Series(list(ascii_uppercase), map(lambda x: 'Letter_' + x, list(ascii_uppercase)))


labeled_values.get('Letter_O')
labeled_values.get('Letter_O', default=None)
labeled_values.loc['Letter_O']
labeled_values['Letter_O']