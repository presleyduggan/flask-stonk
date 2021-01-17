import numpy as np
import matplotlib.pyplot as plt

x = np.arange(10)
y = np.arange(10) * 0.1

mask1 = y < 0.5
mask2 = y >= 0.5

print(mask1)

plt.bar(x[mask1], y[mask1], color = 'red')
plt.bar(x[mask2], y[mask2], color = 'blue')
plt.show()