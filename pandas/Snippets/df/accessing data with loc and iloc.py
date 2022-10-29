nutrition.set_index('name', drop=True).iloc[3:5, 4:6]
nutrition.set_index('name', drop=True).loc['Cornstarch':'Sherbet, orange','cholesterol':'fat']

# Or

nutrition.loc[
              ['Raspberries, raw', 'Blackberries, raw'],
              ['protein', 'vitamin_b6', 'water']
]


# iloc
nutrition.iloc[3]
nutrition.iloc[[4,6,9], 2]
nutrition.iloc[[4,6,9], 2:5]

# boolean mask

new_nutr = nutrition.iloc[
               [True if i%2==0 else False for i in range(8789)],
               [True if i%2==0 else False for i in range(75)]
]

