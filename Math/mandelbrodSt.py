import numpy as np
import matplotlib.pyplot as plt


def mandelbrot(c, max_iter):
    """
    Determines whether a particular complex number is part of the Mandelbrot set.
    :param c: Complex number.
    :param max_iter: Maximum number of iterations to check.
    :return: Number of iterations or max_iter.
    """
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z * z + c
    return max_iter


def generate_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter):
    """
    Generates the Mandelbrot set.
    :param width: Width of the image.
    :param height: Height of the image.
    :param x_min: Minimum x-coordinate.
    :param x_max: Maximum x-coordinate.
    :param y_min: Minimum y-coordinate.
    :param y_max: Maximum y-coordinate.
    :param max_iter: Maximum number of iterations.
    :return: 2D array containing iteration counts.
    """
    r1 = np.linspace(x_min, x_max, width)
    r2 = np.linspace(y_min, y_max, height)
    n_mandelbrot = np.empty((width, height))

    for i in range(width):
        for j in range(height):
            n_mandelbrot[i, j] = mandelbrot(r1[i] + 1j * r2[j], max_iter)

    return n_mandelbrot


# Parameters
width, height = 800, 800
x_min, x_max, y_min, y_max = -2.0, 1.0, -1.5, 1.5
max_iter = 100

# Generate Mandelbrot set
mandelbrot_set = generate_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter)

# Plot the Mandelbrot set
plt.figure(figsize=(10, 10))
plt.imshow(mandelbrot_set.T, extent=[x_min, x_max, y_min, y_max], origin='lower', cmap='hot', interpolation='bilinear')
plt.colorbar(label='Number of iterations')
plt.title('Mandelbrot Set')
plt.xlabel('Re')
plt.ylabel('Im')
plt.show()
