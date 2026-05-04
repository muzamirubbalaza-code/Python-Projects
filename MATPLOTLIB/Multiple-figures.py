import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

x1 , y1 = np.random.random(100) , np.random.random(100)
x2 , y2 = np.random.random(100) , np.random.random(100)

style.use('ggplot')
plt.figure(1)
plt.scatter(x1, y1, color='b', label='Dataset 1')

plt.figure(2)
plt.plot(x2, y2, marker='o', linestyle='-', color='r', label='Dataset 2')

plt.show()