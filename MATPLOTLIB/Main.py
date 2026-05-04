import numpy as np
import matplotlib.pyplot as plt

# Plotting a simple scatter graph
x_data = np.random.random(50) * 100 # Generate 50 random x values between 0 and 100
y_data = np.random.random(50) * 100
plt.scatter(x_data, y_data, color='blue', marker='o',s=100, alpha=0.5)
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid()
plt.show()