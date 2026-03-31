import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create figure and axis
fig, ax = plt.subplots()

# Set axis limits
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Circle properties
x, y = 0, 5
circle = plt.Circle((x, y), 0.5, color='blue')
ax.add_patch(circle)

paused = False

# Initialization function
def init():
    circle.center = (0, 5)
    return circle,

# Animation function
def animate(frame):
    global x
    if not paused:
        x += 0.05
        if x > 10:
            x = 0
        circle.center = (x, y)
    return circle,


def on_key(event):
    global x, y, paused

    if event.key == ' ':
        paused = not paused

    elif event.key == 'left':
        x -= 0.5

    elif event.key == 'right':
        x += 0.5

    elif event.key == 'up':
        y += 0.5

    elif event.key == 'down':
        y -= 0.5

    circle.center = (x, y)
    fig.canvas.draw_idle()

# Connect keyboard event
fig.canvas.mpl_connect('key_press_event', on_key)

# Create animation
ani = animation.FuncAnimation(
    fig,
    animate,
    frames=120,
    init_func=init,
    interval=30,
    blit=True
)

# Show animation
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.show()
