import numpy as np
import matplotlib.pyplot as plt

years = list(range(2010, 2020))

income = [ 50000 , 55000 , 60000 , 65000 , 70000 , 75000 , 80000 , 85000 , 90000 , 95000 ]
income_ticks = list(range(50000, 100000, 5000))
plt.plot(years, income, marker='o', linestyle='-', color='b')
plt.title('Income Growth Over Time',fontsize=16)
plt.xlabel('Year')
plt.ylabel('Income ($)')
plt.xticks(years)
plt.yticks(income_ticks)
plt.grid()
plt.show()
