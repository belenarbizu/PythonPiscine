from load_image import ft_load
import cv2
import numpy as np


def rotate(path):
    try:
        print(ft_load(path))
        img = cv2.imread(path)
        img_zoom = img[100:500, 150:550]
        #Cambio la imagen RGB de 3 canales a un solo canal (400,400)
        img_gray = cv2.cvtColor(img_zoom, cv2.COLOR_RGB2GRAY)
        print("New shape after Transpose:", img_gray.shape)
        print(img_gray)
        cv2.imshow('Imagen de entrada', img_gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except Exception as e:
        print("Error:", e)


def main():
    rotate("animal.jpeg")


if __name__ == "__main__":
    main()
