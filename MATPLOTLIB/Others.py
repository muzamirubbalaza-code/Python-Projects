import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

votes = [ 100 , 150 , 200 , 250 , 300 ]
people = [ "Alice" , "Bob" , "Charlie" , "David" , "Eve" ]

style.use('ggplot')
plt.pie(votes, labels=people, autopct='%1.1f%%', startangle=140)
plt.title('Votes Distribution', fontsize=16)
plt.axis('equal')
plt.legend(loc='upper right')
plt.show()