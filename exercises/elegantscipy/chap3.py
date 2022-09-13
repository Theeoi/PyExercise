#!/usr/bin/env python
"""
Exercises from Chapter 3 of Elegant Scipy
By: Theodor Blom
"""
import numpy as np
from skimage import io
import matplotlib.pyplot as plt

URL_COINS = (
    'https://raw.githubusercontent.com/scikit-image/scikit-image/'
    'v0.10.1/skimage/data/coins.png'
)
URL_ASTRONAUT = (
    'https://raw.githubusercontent.com/scikit-image/scikit-image/'
    'master/skimage/data/astronaut.png'
)


def make_some_noise(size_x: int, size_y: int) -> None:
    """
    Plots random noise image of size {size_x} and {size_y}.
    """
    random_image = np.random.rand(size_x, size_y)
    plt.imshow(random_image)


def read_imgurl(url: str) -> np.ndarray:
    """
    Reads image at {url} and return a np.ndarray representation of that image.
    """
    return io.imread(url)


def print_skimage(image: np.ndarray) -> None:
    """
    Prints {image} as a scikit-image.
    """
    print(
        f"Type: {type(image)}\n"
        f"Shape: {image.shape}\n"
        f"Data type: {image.dtype}"
    )
    plt.imshow(image)


def add_square(image: np.ndarray,
               sq_x: tuple[int, int],
               sq_y: tuple[int, int],
               color: tuple[int, int, int]) -> None:
    """
    Adds a square of {color} in RGB to {image} in a square with top-left corner
    {sq_tl} and bottom-right corner {sq_br}.
    """
    image[sq_x[0]:sq_x[1], sq_y[0]:sq_y[1]] = [color]


def overlay_grid(image: np.ndarray, spacing: int = 128) -> None:
    """
    Adds a blue square grid to {image} with {spacing} in pixels.

    This function is part of the exercise on page 55.
    """
    image[spacing:-1:spacing, :] = [0, 0, 255]
    image[:, spacing:-1:spacing] = [0, 0, 255]


if __name__ == "__main__":
    make_some_noise(500, 500)

    image = read_imgurl(URL_ASTRONAUT)
    add_square(image, (50, 100), (50, 100), (0, 255, 0))
    overlay_grid(image)

    plt.imshow(image)
    plt.show()
