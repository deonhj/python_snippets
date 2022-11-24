import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


x = np.random.randn(100000)
print(plt.style.available)
plt.plot(x.cumsum())
plt.show()