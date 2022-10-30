t = pd.Series([True if i%2 ==0 else False for i in range(10)])
f = pd.Series([True for i in range(10)])

t & f
t | f