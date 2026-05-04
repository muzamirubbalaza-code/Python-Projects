import numpy as np
import matplotlib.pyplot as plt

stock_a = [ 95 , 56 , 67 , 90 , 140 ]
stock_b = [ 30 , 27 , 45 , 50 , 60 ]
stock_c = [ 100 , 177 , 134 , 183 , 120 ]

plt.plot(stock_a, marker='o', linestyle='-', color='b', label='Stock A')
plt.plot(stock_b, marker='s', linestyle='--', color='r', label='Stock B')
plt.plot(stock_c, marker='^', linestyle='-.', color='g', label='Stock C')

plt.title('Stock Price Comparison', fontsize=16)
plt.xlabel('Time (Days)')
plt.ylabel('Stock Price ($)')
plt.legend(loc='upper left')
plt.show()
