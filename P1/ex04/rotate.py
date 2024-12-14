from load_image import ft_load
import cv2
import numpy as np


def rotate(path):
    try:
        img = ft_load(path)
        print(img)
        img = np.squeeze(img)  # Convierte a (400, 400)
        rows = len(img)
        columns = len(img[0])
        transposed = [[0] * rows for _ in range(columns)]
        for x in range(rows):
            for y in range(columns):
                transposed[y][x] = img[x][y]
        transarray = np.array(transposed)
        print("New shape after Transpose:", transarray.shape)
        print(transarray)
        cv2.imshow('Imagen de entrada', transarray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except Exception as e:
        print("Error:", e)


def main():
    rotate("animal.jpeg")


if __name__ == "__main__":
    main()
