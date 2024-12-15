import numpy as np

def ft_invert(array)-> np.ndarray:
    """
    Inverts the color of the image received.
    """
    invert_filter = array.copy()
    invert_filter[:, :, 0] = 255 - invert_filter[:, :, 0]
    invert_filter[:, :, 1] = 255 - invert_filter[:, :, 1]
    invert_filter[:, :, 2] = 255 - invert_filter[:, :, 2]
    return invert_filter

def ft_red(array)-> np.ndarray:
    """
    Changes the image to red.
    """
    red_filter = array.copy()
    red_filter[:,:,0] = red_filter[:,:,0] * 0
    red_filter[:,:,1] = red_filter[:,:,1] * 0
    red_filter[:, :, 2] = np.clip(red_filter[:, :, 2] * 1, 0, 255) 
    return red_filter

def ft_green(array)-> np.ndarray:
    """
    Changes the image to green.
    """
    green_filter = array.copy()
    green_filter[:,:,0] -= green_filter[:, :, 0]
    green_filter[:, :, 2] -= green_filter[:, :, 2]

    return green_filter

def ft_blue(array)-> np.ndarray:
    """
    Changes the image to blue.
    """
    blue_filter = array.copy()
    blue_filter[:,:,1] = 0
    blue_filter[:, :, 2] = 0

    return blue_filter

def ft_grey(array)-> np.ndarray:
    """
    Changes the image to grey.
    """
    grey_filter = array.copy()
    grey_filter[:, :, 0] = grey_filter[:, :, 1]
    grey_filter[:, :, 2] = grey_filter[:, :, 1]

    return grey_filter
