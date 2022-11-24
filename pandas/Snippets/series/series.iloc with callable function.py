def every_fifth(x):
    return [True if i%5==0 else False for i in range(len(x))]

labeled_values.iloc[every_fifth]


# Other example
def every_fifth(x):
    return [True if (i+1)%5==0 else False for i in range(len(x))]

labeled_values.iloc[every_fifth]