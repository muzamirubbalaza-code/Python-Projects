import numpy as np
import matplotlib.pyplot as plt

ages = np.random.normal(20, 1.5, 1000)
plt.hist(ages,color="blue", edgecolor="black") # For the cummulative histogram, add cumulative=True
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.grid(alpha=0.5)
plt.show()