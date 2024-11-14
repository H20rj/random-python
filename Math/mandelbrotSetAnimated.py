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


# Set initial zoom parameters focused near an edge region
center_x, center_y = -0.743643887037151, 0.13182590420533  # Seahorse Valley coordinates
zoom_factor = 0.98  # Smaller zoom per frame for extended zooming
frames = 400  # Increased number of frames for deeper zoom
width, height = 800, 800  # Image dimensions
max_iter = 100  # Maximum number of iterations
fps = 15  # Keep the same playback speed

# Initial zoom range
zoom_range = 3.0

# Create a figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.axis("off")


# Function to update each frame
def update(frame):
    global zoom_range
    ax.clear()  # Clear the axis
    ax.axis("off")

    # Calculate new bounds based on the current zoom range
    xmin = center_x - zoom_range / 2
    xmax = center_x + zoom_range / 2
    ymin = center_y - zoom_range / 2
    ymax = center_y + zoom_range / 2

    # Generate and display the Mandelbrot set
    m_set = mandelbrot_image(xmin, xmax, ymin, ymax, width, height, max_iter)
    ax.imshow(m_set, extent=(xmin, xmax, ymin, ymax), cmap="twilight_shifted")

    # Zoom in for the next frame
    zoom_range *= zoom_factor  # Reduce the zoom range for the next frame


# Create the animation
ani = FuncAnimation(fig, update, frames=frames, repeat=False)
ani.save("mandelbrot_zoom_edge_long.gif", writer="pillow", fps=fps)

print("Animation saved as 'mandelbrot_zoom_edge_long.gif'")
