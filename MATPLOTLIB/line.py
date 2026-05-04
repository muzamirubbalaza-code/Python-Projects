import numpy as np
import matplotlib.pyplot as plt

# years = list(range(2010,2025))
# years = [2015 + x for x in range(16)]
years = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
weights = [68, 70, 72, 75, 78, 80, 77, 74, 73, 71]

plt.plot(years, weights, marker='*',c="purple")
plt.title("Weight Change Over Years")
plt.xlabel("Year")
plt.ylabel("Weight (kg)")
plt.grid(True)

plt.show()