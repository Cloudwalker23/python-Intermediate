import sys
import matplotlib
#matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

x = ["APPLES", "BANANAS"]
y = [400, 350,500]

plt.bar(x, y)
plt.show()