import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create figure and axis
fig, ax = plt.subplots()

# Set axis limits
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Create circle
circle = plt.Circle((0, 5), 0.5, color='blue')
ax.add_patch(circle)

# Initialization function
def init():
    circle.center = (0, 5)
    return circle,

# Animation function
def animate(frame):
    x = frame * 0.1   # move circle horizontally
    y = 5
    circle.center = (x, y)
    return circle,

# Create animation
ani = animation.FuncAnimation(
    fig,
    animate,
    frames=100,
    init_func=init,
    interval=30,
    blit=True
)

# Show animation
plt.show()
