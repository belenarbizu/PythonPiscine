from PIL import Image, UnidentifiedImageError
import numpy as np
import cv2


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
    img_zoom = img[100:500, 150:550]
    #Cambio la imagen RGB de 3 canales a un solo canal (400,400)
    img_gray = cv2.cvtColor(img_zoom, cv2.COLOR_RGB2GRAY)
    #Expandimos un canal adicional (400,400,1)
    img_gray_expanded = np.expand_dims(img_gray, axis=-1) 
    print("The shape of image is:", img_gray_expanded.shape)
    return str(img_gray_expanded)
