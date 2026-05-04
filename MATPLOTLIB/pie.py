import numpy as np
import matplotlib.pyplot as plt

languages = ["C++","C#","Python","Java","JavaScript"]
votes = [33,35,70,57,63]
# Plot configurations for the pie chart
explodes = [0.1, 0.1, 0.1, 0.1, 0.1] # Explode all slices for better visibility

plt.pie(votes, labels=languages, autopct="%1.1f%%", startangle=140, colors=["red","green","blue","orange","purple"], explode=explodes,shadow=True,pctdistance=0.85)
plt.title("Programming Language Popularity")
plt.axis("equal") # Equal aspect ratio ensures that pie chart is circular.
plt.show()