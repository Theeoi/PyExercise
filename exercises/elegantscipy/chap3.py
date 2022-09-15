#!/usr/bin/env python
"""
Exercises and example code from Chapter 3 of Elegant Scipy
By: Theodor Blom
"""
import time

import numpy as np
from skimage import io
from scipy import ndimage as ndi
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


def sobel_convolution(image: np.ndarray) -> None:
    """
    Performs sobel convolution (edge-detection) on {image} and plots the
    result.
    """
    hsobel = np.array(
        [
            [1, 2, 1],
            [0, 0, 0],
            [-1, -2, -1]
        ]
    )
    vsobel = hsobel.T

    # Prevent overflow issues
    image = image.astype(float) / 255

    image_h = ndi.convolve(image, hsobel)
    image_v = ndi.convolve(image, vsobel)
    image_sobel = np.sqrt(image_h**2 + image_v**2)

    fig = plt.figure()
    gs = plt.GridSpec(2, 2, figure=fig, height_ratios=[1, 3])
    ax1 = fig.add_subplot(gs[0, 0])
    ax2 = fig.add_subplot(gs[0, 1])
    ax3 = fig.add_subplot(gs[1, :])
    ax1.imshow(image_h, cmap=plt.cm.RdBu)
    ax2.imshow(image_v, cmap=plt.cm.RdBu)
    ax3.imshow(image_sobel)


def generate_grid(x, y, seed: int | None) -> np.ndarray:
    """
    Return a random ndarray of size {x} and {y} with black and white squares.
    Optionally takes kwarg "seed: int".
    """
    rng = np.random.default_rng(seed)

    grid = rng.integers(0, 1, (x, y), endpoint=True)

    return grid


def nextgen_filter(values: np.ndarray) -> int:
    """
    Returns integer for live (1) or dead (0) for center pixel depending on
    neighbouring {values}.
    """
    center = values[len(values) // 2]
    neighbour_count = np.sum(values) - center
    if neighbour_count == 3 or (center and neighbour_count == 2):
        return 1

    return 0


def next_generation(gen: np.ndarray) -> np.ndarray:
    """
    Return the next generation conway_game from {gen}
    """
    return ndi.generic_filter(gen, nextgen_filter, size=3, mode='wrap')


def conway_game(size: tuple[int, int],
                generations: int,
                seed: int = None) -> None:
    """
    Implementing the Conway game of life using ndi.generic_filter.

    This function is part of the exercise on page 67.
    """
    plt.ion()

    fig, ax = plt.subplots()
    grid = generate_grid(size[0], size[1], seed)
    img = ax.imshow(grid, cmap='gray')

    for _ in range(generations):
        grid = next_generation(grid)

        img.set_data(grid)
        fig.canvas.draw()
        fig.canvas.flush_events()

        time.sleep(0.1)


if __name__ == "__main__":
    # make_some_noise(500, 500)

    # image_a = read_imgurl(URL_ASTRONAUT)
    # add_square(image_a, (50, 100), (50, 100), (0, 255, 0))
    # overlay_grid(image_a)
    # plt.imshow(image_a)

    # image_c = read_imgurl(URL_COINS)
    # sobel_convolution(image_c)

    conway_game((20, 20), 100)

    plt.show()
