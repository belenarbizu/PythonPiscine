import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def ft_invert(array) -> np.ndarray:
    """
    Inverts the color of the image received.
    """
    invert_filter = array.copy()
    invert_filter = 255 - invert_filter

    im = Image.fromarray(invert_filter, mode="RGB")
    plt.imshow(im)
    plt.show()
    return invert_filter


def ft_red(array) -> np.ndarray:
    """
    Changes the image to red.
    """
    red_filter = array.copy()
    red_filter[:, :, 1] = red_filter[:, :, 1] * 0
    red_filter[:, :, 2] = red_filter[:, :, 2] * 0

    im = Image.fromarray(red_filter, mode="RGB")
    plt.imshow(im)
    plt.show()
    return red_filter


def ft_green(array) -> np.ndarray:
    """
    Changes the image to green.
    """
    green_filter = array.copy()
    green_filter[:, :, 0] -= green_filter[:, :, 0]
    green_filter[:, :, 2] -= green_filter[:, :, 2]

    im = Image.fromarray(green_filter, mode="RGB")
    plt.imshow(im)
    plt.show()
    return green_filter


def ft_blue(array) -> np.ndarray:
    """
    Changes the image to blue.
    """
    blue_filter = array.copy()
    blue_filter[:, :, 0] = 0
    blue_filter[:, :, 1] = 0

    im = Image.fromarray(blue_filter, mode="RGB")
    plt.imshow(im)
    plt.show()
    return blue_filter


def ft_grey(array) -> np.ndarray:
    """
    Changes the image to grey.
    """
    grey_filter = array.copy()
    grey_filter[:, :, 0] = grey_filter[:, :, 1]
    grey_filter[:, :, 2] = grey_filter[:, :, 1]

    im = Image.fromarray(grey_filter, mode="RGB")
    plt.imshow(im)
    plt.show()
    return grey_filter
