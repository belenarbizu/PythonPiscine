from PIL import Image, UnidentifiedImageError
import numpy as np

def ft_load(path: str) -> str:
    """
    Convert the image into an 8-bit numpy array and print the shape
    and its pixels content in RGB format
    """
    try:
        im = Image.open(path)
    except FileNotFoundError:
        raise SystemExit("File not found")
    except UnidentifiedImageError:
        raise SystemExit("Image can't be open and identified")
    except ValueError:
        raise SystemExit("Can't read file")
    except TypeError:
        raise SystemExit("Format image is not correct")

    img = np.asarray(im)
    print("The shape of image is:", img.shape)
    return str(img)