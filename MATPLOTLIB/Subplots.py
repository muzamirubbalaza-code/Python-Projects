import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

x = np.arange(100)
fig , axs = plt.subplots(2, 2)

axs[0, 0].plot(x, np.sin(x))
axs[0, 0].set_title('Sine Wave')

axs[0, 1].plot(x, np.cos(x))
axs[0, 1].set_title('Cosine Wave')

axs[1, 0].plot(x, np.tan(x))
axs[1, 0].set_title('Tangent Wave')

axs[1, 1].plot(x, np.exp(x/20))
axs[1, 1].set_title('Exponential Growth')

plt.suptitle('Multiple Subplots Example', fontsize=16)

# To export the figure as an image file, you can use the following line:
# plt.savefig('subplots_example.png', dpi=300, transparent=True, bbox_inches='tight')
# The parameters used in plt.savefig() are:
# 'subplots_example.png': The name of the output file.
# dpi=300: Sets the resolution of the saved image to 300 dots per inch.
# transparent=True: Makes the background of the saved image transparent.
# bbox_inches='tight': Adjusts the bounding box to fit the content of the figure tightly, removing any extra whitespace.
# After running the above code, you will find a file named 'subplots_example.png' in your current working directory, containing the generated subplots with the specified settings.
plt.tight_layout()  # Adjust layout to prevent overlap

plt.show()