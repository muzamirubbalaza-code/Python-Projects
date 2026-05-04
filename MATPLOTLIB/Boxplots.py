import numpy as np
import matplotlib.pyplot as plt

heights = np.random.normal(172,8,300)
plt.boxplot(heights, vert=True, patch_artist=True, boxprops=dict(facecolor="lightblue", color="blue"), medianprops=dict(color="red", linewidth=2), whiskerprops=dict(color="blue", linewidth=1.5), capprops=dict(color="blue", linewidth=1.5))
plt.title("Height Distribution")
plt.ylabel("Height (cm)")
plt.grid(alpha=0.5)
plt.show()