import matplotlib.pyplot as plt
import numpy as np

sizes = [35, 25, 25, 15]
labels = ['Apples', 'Bananas', 'Cherries', 'Dates']

plt.pie(sizes, labels=labels)
plt.show()