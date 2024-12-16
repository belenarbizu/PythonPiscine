import numpy as np
import cv2


def ft_load(path: str) -> np.ndarray:
    """
    Convert the image into an 8-bit numpy array and print the shape
    and its pixels content in RGB format
    """
    try:
        im = cv2.imread(path)
    except FileNotFoundError:
        raise SystemExit("File not found")
    except ValueError:
        raise SystemExit("Can't read file")
    except TypeError:
        raise SystemExit("Format image is not correct")

    img = np.asarray(im)
    print("The shape of image is:", img.shape)
    print(img)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img_rgb
