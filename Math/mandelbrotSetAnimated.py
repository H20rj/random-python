import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Function to calculate the Mandelbrot set
def mandelbrot(c, max_iter):
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

# Function to create an image of the Mandelbrot set
def mandelbrot_image(xmin, xmax, ymin, ymax, width, height, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    n3 = np.empty((height, width))
    for i in range(width):
        for j in range(height):
            c = r1[i] + 1j * r2[j]
            n3[j, i] = mandelbrot(c, max_iter)
    return n3

# Set the parameters for the initial image
width, height = 800, 800
max_iter = 100
frames = 100

# Set the point to zoom into (e.g., "Seahorse Valley")
x_center, y_center = -0.743643887037151, 0.131825904205330

# Set initial zoom level and zoom factor
zoom = 1
zoom_factor = 0.9  # Controls how much we zoom in each frame

# Create a figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.axis("off")

# Function to update each frame
def update(frame):
    global zoom
    ax.clear()
    ax.axis("off")

    # Calculate the current zoom level
    zoom *= zoom_factor

    # Calculate the current window
    x_range = 3.5 * zoom
    y_range = 3.5 * zoom

    xmin = x_center - x_range / 2
    xmax = x_center + x_range / 2
    ymin = y_center - y_range / 2
    ymax = y_center + y_range / 2

    # Generate and display the Mandelbrot set
    m_set = mandelbrot_image(xmin, xmax, ymin, ymax, width, height, max_iter)
    ax.imshow(m_set, extent=(xmin, xmax, ymin, ymax), cmap="twilight_shifted", origin='lower')

# Create the animation
ani = FuncAnimation(fig, update, frames=frames, repeat=False)
ani.save("mandelbrot_zoom.gif", writer="pillow", fps=15)

print("Animation saved as 'mandelbrot_zoom.gif'")
