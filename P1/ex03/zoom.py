from load_image import ft_load
import cv2


def zoom(path):
    print(ft_load(path))
    try:
        img = cv2.imread(path)
        image_cropped = img[100:500, 400:800]
        print("New shape after slicing:", image_cropped.shape)
        cv2.imshow('Imagen redimensionada', image_cropped)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except:
        print("Error")


def main():
    zoom("animal.jpeg")


if __name__ == "__main__":
    main()
