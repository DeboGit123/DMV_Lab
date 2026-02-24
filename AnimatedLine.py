import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create a figure and axis
fig, ax = plt.subplots()
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

# Create an empty line object
line, = ax.plot(x, y)

# Update function for animation
def update(frame):
    line.set_ydata(np.sin(x + frame/10))  # shift the sine wave
    return line,

# Create animation
ani = FuncAnimation(fig, update, frames=100, interval=50, blit=True)

plt.show()
