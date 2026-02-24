import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y1 = [1, 4, 9, 16]
y2 = [2, 3, 5, 7]

plt.subplot(1, 2, 1)
plt.plot(x, y1)
plt.title("Plot 1")

plt.subplot(1, 2, 2)
plt.plot(x, y2)
plt.title("Plot 2")

plt.show()