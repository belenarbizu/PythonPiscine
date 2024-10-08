from load_image import ft_load
import cv2
import numpy as np

def zoom(path):
    print(ft_load(path))
    try:
        img = cv2.imread(path)
    except:
        print("Error")
    img_zoom = cv2.resize(img, (400,400))
    cv2.imshow(img_zoom)


def main():
    zoom("animal.jpeg")

if __name__ == "__main__":
    main()