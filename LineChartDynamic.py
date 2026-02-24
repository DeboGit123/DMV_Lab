import matplotlib.pyplot as plt
import numpy as np

x = []
y = []

n = int(input("Enter the number of points :"))

for i in range(n):
    x.append(int(input("Enter x :")))

for i in range(n):
    y.append(int(input("Enter y :")))

plt.plot(x,y)
plt.sdetter(x,y)
plt.show()