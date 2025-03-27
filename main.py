import numpy as np
import matplotlib.pyplot as plt
import colorsys

def visualize_hue_spectrum(num_points=360, brightness=1.0, saturation=1.0):
    """
    Visualizes the hue spectrum as a circular gradient.

    Args:
        num_points: Number of points to sample in the hue spectrum.
        brightness: Brightness of the colors (0.0 to 1.0).
        saturation: Saturation of the colors (0.0 to 1.0).
    """

    hues = np.linspace(0, 1, num_points, endpoint=False)  # Hue values from 0 to 1
    rgb_colors = [colorsys.hsv_to_rgb(h, saturation, brightness) for h in hues]

    # Create a circular plot
    theta = np.linspace(0, 2 * np.pi, num_points, endpoint=False)
    x = np.cos(theta)
    y = np.sin(theta)

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.scatter(x, y, c=rgb_colors, s=200)  # Adjust 's' for dot size

    ax.set_aspect('equal')
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.axis('off')  # Turn off axis labels and ticks

    # Add a center point (optional)
    ax.scatter([0], [0], c='white', s=50)

    # Add a title
    plt.title("Hue Spectrum Visualization")

    plt.show()

def visualize_hue_wave(num_points=1000, brightness=1.0, saturation=1.0):
    """
    Visualizes the hue spectrum as a horizontal wave.

    Args:
        num_points: Number of points to sample.
        brightness: Brightness of the colors.
        saturation: Saturation of the colors.
    """

    hues = np.linspace(0, 1, num_points)
    rgb_colors = [colorsys.hsv_to_rgb(h, saturation, brightness) for h in hues]

    x = np.linspace(0, 10, num_points)
    y = np.sin(x)  # Using a sine wave for visual effect

    plt.figure(figsize=(12, 6))
    plt.scatter(x, y, c=rgb_colors, s=20)
    plt.title("Hue Spectrum Wave")
    plt.xlabel("Position")
    plt.ylabel("Amplitude")
    plt.show()

def visualize_hue_gradient(width=800, height=50):
    """
    Visualizes the hue spectrum as a horizontal gradient.

    Args:
        width: Width of the gradient.
        height: Height of the gradient.
    """
    
    gradient = np.zeros((height, width, 3), dtype=np.uint8)
    for x in range(width):
        hue = x / width
        r, g, b = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
        gradient[:, x, 0] = int(r * 255)
        gradient[:, x, 1] = int(g * 255)
        gradient[:, x, 2] = int(b * 255)

    plt.figure(figsize=(10, 2))
    plt.imshow(gradient)
    plt.axis('off')
    plt.title("Hue Gradient")
    plt.show()

# Example usages:
visualize_hue_spectrum()
visualize_hue_wave()
visualize_hue_gradient()