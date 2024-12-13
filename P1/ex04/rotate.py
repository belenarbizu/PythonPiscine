from load_image import ft_load
import cv2
import numpy as np


def rotate(path):
    try:
        img = ft_load(path)
        print(img)
        rows = len(img)
        columns = len(img[0])
        transposed = np.zeros((columns, rows))
        for x in range(rows):
            for y in range(columns):
                transposed[x][y] = img[x][y]
        print("New shape after Transpose:", img.shape)
        print(transposed)
        cv2.imshow('Imagen de entrada', transposed)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except Exception as e:
        print("Error:", e)


def main():
    rotate("animal.jpeg")


if __name__ == "__main__":
    main()
