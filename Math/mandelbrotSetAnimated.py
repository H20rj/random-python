import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from PIL import Image


# Function to calculate the Mandelbrot set
def mandelbrot(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z * z + c
    return max_iter


# Function to create an image of the Mandelbrot set
def mandelbrot_image(xmin, xmax, ymin, ymax, width, height, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    n3 = np.empty((width, height))
    for i in range(width):
        for j in range(height):
            n3[i, j] = mandelbrot(r1[i] + 1j * r2[j], max_iter)
    return (n3.T)


# Set initial zoom parameters
xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5
zoom_factor = 0.9  # Controls how much we zoom in each frame
frames = 100  # Number of frames in the animation
width, height = 800, 800  # Image dimensions
max_iter = 100  # Maximum number of iterations

# Create a figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.axis("off")


# Function to update each frame
def update(frame):
    global xmin, xmax, ymin, ymax
    ax.clear()  # Clear the axis
    ax.axis("off")

    # Generate and display the Mandelbrot set
    m_set = mandelbrot_image(xmin, xmax, ymin, ymax, width, height, max_iter)
    ax.imshow(m_set, extent=(xmin, xmax, ymin, ymax), cmap="twilight_shifted")

    # Zoom in for the next frame
    x_range = (xmax - xmin) * zoom_factor
    y_range = (ymax - ymin) * zoom_factor
    xmin += x_range * 0.1
    xmax -= x_range * 0.1
    ymin += y_range * 0.1
    ymax -= y_range * 0.1


# Create the animation
ani = FuncAnimation(fig, update, frames=frames, repeat=False)
ani.save("mandelbrot_zoom.gif", writer="pillow", fps=15)

print("Animation saved as 'mandelbrot_zoom.gif'")
