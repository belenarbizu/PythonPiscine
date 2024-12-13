from load_image import ft_load
import cv2
import numpy as np


def zoom(path):
    try:
        print(ft_load(path))
        img = cv2.imread(path)
        img_zoom = img[100:500, 150:550]
        #Cambio la imagen RGB de 3 canales a un solo canal (400,400)
        img_gray = cv2.cvtColor(img_zoom, cv2.COLOR_RGB2GRAY)
        #Expandimos un canal adicional (400,400,1)
        img_gray_expanded = np.expand_dims(img_gray, axis=-1) 
        print("New shape after slicing:", img_gray_expanded.shape)
        print(img_gray_expanded)
    except Exception as e:
        print("Error:", e)


def main():
    zoom("animal.jpeg")


if __name__ == "__main__":
    main()
