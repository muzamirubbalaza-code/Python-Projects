import numpy as np
import matplotlib.pyplot as plt

x = ["C++","C#","Python","Java","JavaScript"]
y = ["33","35","70","57","63"]

plt.bar(x,y,color=["red","green","blue","orange","purple"],align="center",width=0.5)
plt.title("Programming Language Popularity")
plt.xlabel("Programmimg_Languages")
plt.ylabel("Popularity (%)")
plt.grid(alpha=0.5)
plt.show()